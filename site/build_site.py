#!/usr/bin/env python3
"""
Build the CCDAK study site.

  python3 build_site.py

Reads  ../<N>.<module>/*-summary.md  (N = 1..12) and ../EXAM-SCOPE.md,
renders them to HTML and writes:
  index.html  - study site (summaries, search, progress, exam tab)
  exam.html   - copy of ../exams/exam-test-aggregate.html (run ../exams/build.sh first)

Requires:  pip install markdown-it-py
"""
import os, re, json, glob, shutil, base64, sys
from markdown_it import MarkdownIt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

MODULES = [
    ("1", "1.broker", "Broker", "Brokers, replication, ISR, retention, KRaft, request lifecycle", "core"),
    ("2", "2.consumer", "Consumer", "Consumer groups, assignors, offsets, rebalancing, delivery semantics", "core"),
    ("3", "3.producer", "Producer", "acks, idempotence, transactions, partitioner, serialization, headers", "core"),
    ("4", "4.topic", "Topic", "Topic configs, compaction, partitions, modifying topics", "core"),
    ("5", "5.cli", "CLI & Testing", "CLI tools, testing tools, scaling, deployment frameworks", "core"),
    ("6", "6.kafka-streams", "Kafka Streams", "KStream/KTable, state, EOS, DSL vs Processor API", "core"),
    ("7", "7.kafka-connect", "Kafka Connect", "Workers, connectors, SMT, REST API, offsets, scalability", "core"),
    ("8", "8.security", "Security", "SSL, SASL, ACLs, JAAS", "core"),
    ("9", "9.schema-registry", "Schema Registry", "Avro, compatibility, subjects, REST API", "core"),
    ("10", "10.rest-proxy", "REST Proxy", "HTTP access to Kafka (outside exam scope)", "extra"),
    ("11", "11.monitoring-metrics", "Monitoring & Metrics", "JMX metrics, lag, logging, errors, alerts", "core"),
    ("12", "12.cluster-administration", "Cluster Admin", "Controller, leader balancing, internal topics (outside exam scope)", "extra"),
]

# exam-scope item (prefix) -> module ids that cover it
SCOPE_MAP = {
    "Connect to a secured": ["8", "1"],
    "Understand delivery guarantees": ["3", "2", "6"],
    "Demonstrate how consumer groups": ["2", "1"],
    "Define topics configurations": ["4", "1"],
    "Handle consumer group offsets": ["2", "5"],
    "Understand the purpose of a producer partitioner": ["3", "4"],
    "Explain the difference between consumer assign": ["2"],
    "Understand the relationship of the Apache Kafka resource": ["1"],
    "Explain the lifecycle of a request": ["1"],
    "Identify producer configurations": ["3"],
    "Understand serialization": ["3", "2", "9"],
    "Serialize and deserialize": ["3", "2", "9"],
    "Describe transactions": ["3", "2", "6"],
    "Configure consumer groups": ["2"],
    "Design keys": ["3", "4"],
    "Design headers": ["3"],
    "Consume messages": ["2"],
    "Identify common data formats": ["3", "9"],
    "Apply error handling": ["3", "2", "7", "11"],
    "Understand best practices for modifying topics": ["4"],
    "Define data partitioning": ["4", "3", "6"],
    "Differentiate Apache Kafka streams": ["6"],
    "Describe stateful and stateless": ["6"],
    "Explain exactly once specifically": ["6"],
    "Compare streams and tables": ["6"],
    "Compare DSL and processor": ["6"],
    "Create and configure connectors": ["7"],
    "Design source and sink": ["7"],
    "Define worker properties": ["7"],
    "Explain connector scalability": ["7"],
    "Understand connect offsets": ["7"],
    "Explain Single Message": ["7"],
    "Utilize the Connect REST": ["7"],
    "Understand common testing tools": ["5"],
    "Use CLI tools": ["5"],
    "Apply horizontal and vertical": ["5", "6", "7"],
    "Understand common deployment": ["5"],
    "Understand lag": ["11", "2"],
    "Understand performance metrics": ["11", "1"],
    "Configure logging": ["11"],
    "Understand common errors": ["11", "3"],
    "Configure alerts": ["11"],
}

md = MarkdownIt("commonmark", {"html": True}).enable("table")


def img_data_uri(src):
    path = os.path.normpath(os.path.join(ROOT, re.sub(r"^(\./|\.\./)+", "", src)))
    if not os.path.exists(path):
        return src
    ext = path.rsplit(".", 1)[-1].lower()
    mime = {"svg": "image/svg+xml", "png": "image/png"}.get(ext, "application/octet-stream")
    return "data:%s;base64,%s" % (mime, base64.b64encode(open(path, "rb").read()).decode())


def render_module(folder):
    files = glob.glob(os.path.join(ROOT, folder, "*summary*.md"))
    if not files:
        return "<p>No summary found.</p>"
    html = md.render(open(files[0], encoding="utf-8").read())
    return re.sub(r'(<img[^>]*src=")([^"]+)(")', lambda m: m.group(1) + img_data_uri(m.group(2)) + m.group(3), html)


def parse_scope():
    domains, cur = [], None
    for line in open(os.path.join(ROOT, "EXAM-SCOPE.md"), encoding="utf-8"):
        line = line.rstrip()
        m = re.match(r"##\s+(\d+)\.\s+(.*)", line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2).strip(), "items": []}
            domains.append(cur)
        elif line.lstrip().startswith("- ") and cur is not None:
            item = line.lstrip()[2:].strip()
            mods = []
            for k, v in SCOPE_MAP.items():
                if item.startswith(k):
                    mods = v
                    break
            cur["items"].append({"text": item, "modules": mods})
    return domains


def main():
    mods = []
    for mid, folder, title, desc, kind in MODULES:
        html = render_module(folder)
        words = len(re.sub(r"<[^>]+>", " ", html).split())
        mods.append({"id": mid, "folder": folder, "title": title, "desc": desc, "kind": kind,
                     "html": html, "minutes": max(1, round(words / 200))})
    data = {"modules": mods, "domains": parse_scope()}
    tpl = open(os.path.join(HERE, "site-template.html"), encoding="utf-8").read()
    out = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
    src = os.path.join(ROOT, "exams", "exam-test-aggregate.html")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(HERE, "exam.html"))
    else:
        print("WARNING: exam-test-aggregate.html missing - run exams/build.sh first", file=sys.stderr)
    print("Built index.html (%d KB)" % (len(out) // 1024))


if __name__ == "__main__":
    main()
