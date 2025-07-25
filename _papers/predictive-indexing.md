---
layout: paper_detail
title: "Predictive Indexing"
date: 2019-01-21
arxiv_url: http://arxiv.org/abs/1901.07064v1
---

There has been considerable research on automated index tuning in database management systems (DBMSs). But the majority of these solutions tune the index configuration by retrospectively making computationally expensive physical design changes all at once. Such changes degrade the DBMS's performance during the process, and have reduced utility during subsequent query processing due to the delay between a workload shift and the associated change. A better approach is to generate small changes that tune the physical design over time, forecast the utility of these changes, and apply them ahead of time to maximize their impact.   This paper presents predictive indexing that continuously improves a database's physical design using lightweight physical design changes. It uses a machine learning model to forecast the utility of these changes, and continuously refines the index configuration of the database to handle evolving workloads. We introduce a lightweight hybrid scan operator with which a DBMS can make use of partially-built indexes for query processing. Our evaluation shows that predictive indexing improves the throughput of a DBMS by 3.5--5.2x compared to other state-of-the-art indexing approaches. We demonstrate that predictive indexing works seamlessly with other lightweight automated physical design tuning methods.
