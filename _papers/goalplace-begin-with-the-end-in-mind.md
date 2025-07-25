---
layout: paper_detail
title: "GOALPlace: Begin with the End in Mind"
date: 2024-07-05
arxiv_url: http://arxiv.org/abs/2407.04579v1
---

Co-optimizing placement with congestion is integral to achieving high-quality designs. This paper presents GOALPlace, a new learning-based general approach to improving placement congestion by controlling cell density. Our method efficiently learns from an EDA tool's post-route optimized results and uses an empirical Bayes technique to adapt this goal/target to a specific placer's solutions, effectively beginning with the end in mind. It enhances correlation with the long-running heuristics of the tool's router and timing-opt engine -- while solving placement globally without expensive incremental congestion estimation and mitigation methods. A statistical analysis with a new hierarchical netlist clustering establishes the importance of density and the potential for an adequate cell density target across placements. Our experiments show that our method, integrated as a demonstration inside an academic GPU-accelerated global placer, consistently produces macro and standard cell placements of superior or comparable quality to commercial tools. Our empirical Bayes methodology also allows a substantial quality improvement over state-of-the-art academic mixed-size placers, achieving up to 10x fewer design rule check (DRC) violations, a 5% decrease in wirelength, and a 30% and 60% reduction in worst and total negative slack (WNS/TNS).
