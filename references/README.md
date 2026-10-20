# Sources and credits

The sole evidential source for this reading guide is [What is test-time compute and how to scale it?](https://huggingface.co/blog/Kseniase/testtimecompute), a **Hugging Face Community Article** published on **February 6, 2025**. Its footer credits **[Alyona Vert](https://huggingface.co/alyona0l) as author** and **[Ksenia Se](https://huggingface.co/Kseniase) as editor**. The article is an explanatory blog overview, not an original research paper. This repository's explanations, examples, exercises, and interpretations are independent guide material.

Use [article.bib](article.bib) to cite the article and [references.json](../metadata/references.json) for machine-readable identities, author credits, roles, and verification notes. The access date is October 20, 2026. The source article and its figures retain their respective authors' rights; they are linked rather than republished here. No source PDF is distributed.

## How to read the reference list

The underlying works deserve credit for their methods. Their presence in this list does **not** mean that this repository has read their full texts, reproduced their experiments, or independently established the article's reported results. For the main works, an authoritative arXiv abstract page was inspected to verify bibliographic identity and author credits. This is **bibliographic verification only**.

The selected version links below make the metadata inspection explicit. They do not establish which exact versions the article consulted. In particular, later arXiv revisions can change author lists and reported results. PARM's January 2025 v1 author list is retained rather than substituting its expanded July 2025 list.

For the five additional resources, the article-provided Hugging Face paper pages are retained, with author-list links instead of unverified names. An empty `authors` array in their JSON records means **not transcribed or verified here**. It does not imply anonymous work. `metadata_verified: false` preserves that distinction.

## Main research credits

| ID | Work and authoritative metadata | Credit | Inspection |
| --- | --- | --- | --- |
| `o1-system-card` | [OpenAI o1 System Card](https://arxiv.org/abs/2412.16720v1) | OpenAI; the linked page contains the extensive named author list | Abstract-page bibliography only |
| `deepseek-r1` | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948v1) | DeepSeek-AI; the linked page contains the extensive named author list | Abstract-page bibliography only |
| `virgo` | [Virgo: A Preliminary Exploration on Reproducing o1-like MLLM](https://arxiv.org/abs/2501.01904v2) | Yifan Du, Zikang Liu, Yifan Li, Wayne Xin Zhao, Yuqi Huo, Bingning Wang, Weipeng Chen, Zheng Liu, Zhongyuan Wang, and Ji-Rong Wen | Full named author list from abstract page |
| `mulberry` | [Mulberry: Empowering MLLM with o1-like Reasoning and Reflection via Collective Monte Carlo Tree Search](https://arxiv.org/abs/2412.18319v2) | Huanjin Yao, Jiaxing Huang, Wenhao Wu, Jingyi Zhang, Yibo Wang, Shunyu Liu, Yingjie Wang, Yuxin Song, Haocheng Feng, Li Shen, and Dacheng Tao | Full named author list from abstract page |
| `parm` | [Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step](https://arxiv.org/abs/2501.13926v1) | Ziyu Guo, Renrui Zhang, Chengzhuo Tong, Zhizheng Zhao, Peng Gao, Hongsheng Li, and Pheng-Ann Heng | Full v1 named author list from abstract page |
| `search-o1` | [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://arxiv.org/abs/2501.05366v1) | Xiaoxi Li, Guanting Dong, Jiajie Jin, Yuyao Zhang, Yujia Zhou, Yutao Zhu, Peitian Zhang, and Zhicheng Dou | Full named author list from abstract page; paper identity resolved separately by exact title |
| `sana-1-5` | [SANA 1.5: Efficient Scaling of Training-Time and Inference-Time Compute in Linear Diffusion Transformer](https://arxiv.org/abs/2501.18427v1) | Enze Xie, Junsong Chen, Yuyang Zhao, Jincheng Yu, Ligeng Zhu, Yujun Lin, Zhekai Zhang, Muyang Li, Junyu Chen, Han Cai, Bingchen Liu, Daquan Zhou, and Song Han | Full named author list from abstract page |
| `s1` | [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393v1) | Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto | Full named author list from abstract page |
| `o1-coder` | [o1-Coder: an o1 Replication for Coding](https://arxiv.org/abs/2412.00154v1) | Yuxiang Zhang, Shangxi Wu, Yuqi Yang, Jiangming Shu, Jinlin Xiao, Chao Kong, and Jitao Sang | Full named author list from abstract-page Authors field |

Search-o1 is discussed in the article but lacks a corresponding hyperlink in its bonus resource list. Its primary paper identity was resolved by exact title. That lookup expands the bibliography, not the guide's evidential scope.

## Additional resources linked by the article

These are directions for further reading, not additional evaluated evidence for this guide. The linked paper pages provide author credits and primary-publication links.

| ID | Article-linked resource and full-author entry point |
| --- | --- |
| `underthinking` | [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://huggingface.co/papers/2501.18585) |
| `system-1-system-2` | [Test-time Computing: from System-1 Thinking to System-2 Thinking](https://huggingface.co/papers/2501.02497) |
| `o1-journey-1` | [O1 Replication Journey: A Strategic Progress Report -- Part 1](https://huggingface.co/papers/2410.18982) |
| `o1-journey-2` | [O1 Replication Journey -- Part 2: Surpassing O1-preview through Simple Distillation, Big Progress or Bitter Lesson?](https://huggingface.co/papers/2411.16489) |
| `o1-journey-3` | [O1 Replication Journey -- Part 3: Inference-time Scaling for Medical Reasoning](https://huggingface.co/papers/2501.06458) |

## Citation and update rules

- Attribute an article-reported result to the article. A primary-paper link supplies provenance, not an independent replication claim.
- Mark explanatory deductions and hypothetical examples as guide interpretation.
- If a contributor later checks a full paper, record the version, exact section or table, and scope of verification before changing any evidential status.
- Keep article authorship separate from repository authorship. This repository is not affiliated with or endorsed by the article authors, Hugging Face, or the research teams.

[Return to the guide](../README.md)
