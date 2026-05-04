# Skill Catalog

> 137 skills from K-Dense-AI scientific-agent-skills + claude-scientific-writer
> Each entry: name, description, path to SKILL.md


## Scientific Databases & Data Access

- **database-lookup** - Search 78 public scientific, biomedical, materials science, and economic databases via REST APIs. Covers physics/astr... | `skills/database-lookup/SKILL.md`
- **depmap** - Query the Cancer Dependency Map (DepMap) for cancer cell line gene dependency scores (CRISPR Chronos), drug sensitivi... | `skills/depmap/SKILL.md`
- **imaging-data-commons** - Query and download public cancer imaging data from NCI Imaging Data Commons using idc-index. Use for accessing large-... | `skills/imaging-data-commons/SKILL.md`
- **primekg** - Query the Precision Medicine Knowledge Graph (PrimeKG) for multiscale biological data including genes, drugs, disease... | `skills/primekg/SKILL.md`
- **usfiscaldata** - Query the U.S. Treasury Fiscal Data API for federal financial data including national debt, government spending, reve... | `skills/usfiscaldata/SKILL.md`
- **hugging-science** - Use when the user is doing AI/ML work in a scientific domain — biology, chemistry, physics, astronomy, climate, genom... | `skills/hugging-science/SKILL.md`

## Scientific Integrations

- **benchling-integration** - Benchling R&D platform integration. Access registry (DNA, proteins), inventory, ELN entries, workflows via API, build... | `skills/benchling-integration/SKILL.md`
- **dnanexus-integration** - DNAnexus cloud genomics platform. Build apps/applets, manage data (upload/download), dxpy Python SDK, run workflows, ... | `skills/dnanexus-integration/SKILL.md`
- **opentrons-integration** - Official Opentrons Protocol API for OT-2 and Flex robots. Use when writing protocols specifically for Opentrons hardw... | `skills/opentrons-integration/SKILL.md`
- **ginkgo-cloud-lab** - Submit and manage protocols on Ginkgo Bioworks Cloud Lab (cloud.ginkgo.bio), a web-based interface for autonomous lab... | `skills/ginkgo-cloud-lab/SKILL.md`
- **labarchive-integration** - Electronic lab notebook API integration. Access notebooks, manage entries/attachments, backup notebooks, integrate wi... | `skills/labarchive-integration/SKILL.md`
- **open-notebook** - Self-hosted, open-source alternative to Google NotebookLM for AI-powered research and document analysis. Use when org... | `skills/open-notebook/SKILL.md`
- **latchbio-integration** - Latch platform for bioinformatics workflows. Build pipelines with Latch SDK, @workflow/@task decorators, deploy serve... | `skills/latchbio-integration/SKILL.md`
- **omero-integration** - Microscopy data management platform. Access images via Python, retrieve datasets, analyze pixels, manage ROIs/annotat... | `skills/omero-integration/SKILL.md`
- **protocolsio-integration** - Integration with protocols.io API for managing scientific protocols. This skill should be used when working with prot... | `skills/protocolsio-integration/SKILL.md`

## Bioinformatics & Genomics

- **anndata** - Data structure for annotated matrices in single-cell analysis. Use when working with .h5ad files or integrating with ... | `skills/anndata/SKILL.md`
- **arboreto** - Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3). Use wh... | `skills/arboreto/SKILL.md`
- **biopython** - Comprehensive molecular biology toolkit. Use for sequence manipulation, file parsing (FASTA/GenBank/PDB), phylogeneti... | `skills/biopython/SKILL.md`
- **bioservices** - Unified Python interface to 40+ bioinformatics services. Use when querying multiple databases (UniProt, KEGG, ChEMBL,... | `skills/bioservices/SKILL.md`
- **cellxgene-census** - Query the CELLxGENE Census (61M+ cells) programmatically. Use when you need expression data across tissues, diseases,... | `skills/cellxgene-census/SKILL.md`
- **deeptools** - NGS analysis toolkit. BAM to bigWig conversion, QC (correlation, PCA, fingerprints), heatmaps/profiles (TSS, peaks), ... | `skills/deeptools/SKILL.md`
- **etetoolkit** - Phylogenetic tree toolkit (ETE). Tree manipulation (Newick/NHX), evolutionary event detection, orthology/paralogy, NC... | `skills/etetoolkit/SKILL.md`
- **flowio** - Parse FCS (Flow Cytometry Standard) files v2.0-3.1. Extract events as NumPy arrays, read metadata/channels, convert t... | `skills/flowio/SKILL.md`
- **gget** - Fast CLI/Python queries to 20+ bioinformatics databases. Use for quick lookups: gene info, BLAST searches, AlphaFold ... | `skills/gget/SKILL.md`
- **geniml** - This skill should be used when working with genomic interval data (BED files) for machine learning tasks. Use for tra... | `skills/geniml/SKILL.md`
- **gtars** - High-performance toolkit for genomic interval analysis in Rust with Python bindings. Use when working with genomic re... | `skills/gtars/SKILL.md`
- **phylogenetics** - Build and analyze phylogenetic trees using MAFFT (multiple alignment), IQ-TREE 2 (maximum likelihood), and FastTree (... | `skills/phylogenetics/SKILL.md`
- **polars-bio** - High-performance genomic interval operations and bioinformatics file I/O on Polars DataFrames. Overlap, nearest, merg... | `skills/polars-bio/SKILL.md`
- **pysam** - Genomic file toolkit. Read/write SAM/BAM/CRAM alignments, VCF/BCF variants, FASTA/FASTQ sequences, extract regions, c... | `skills/pysam/SKILL.md`
- **pydeseq2** - Differential gene expression analysis (Python DESeq2). Identify DE genes from bulk RNA-seq counts, Wald tests, FDR co... | `skills/pydeseq2/SKILL.md`
- **scanpy** - Standard single-cell RNA-seq analysis pipeline. Use for QC, normalization, dimensionality reduction (PCA/UMAP/t-SNE),... | `skills/scanpy/SKILL.md`
- **scvelo** - RNA velocity analysis with scVelo. Estimate cell state transitions from unspliced/spliced mRNA dynamics, infer trajec... | `skills/scvelo/SKILL.md`
- **scvi-tools** - Deep generative models for single-cell omics. Use when you need probabilistic batch correction (scVI), transfer learn... | `skills/scvi-tools/SKILL.md`
- **scikit-bio** - Biological data toolkit. Sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ... | `skills/scikit-bio/SKILL.md`
- **tiledbvcf** - Efficient storage and retrieval of genomic variant data using TileDB. Scalable VCF/BCF ingestion, incremental sample ... | `skills/tiledbvcf/SKILL.md`
- **zarr-python** - Chunked N-D arrays for cloud storage. Compressed arrays, parallel I/O, S3/GCS integration, NumPy/Dask/Xarray compatib... | `skills/zarr-python/SKILL.md`

## Data Management & Infrastructure

- **lamindb** - This skill should be used when working with LaminDB, an open-source data framework for biology that makes data querya... | `skills/lamindb/SKILL.md`
- **modal** - Cloud computing platform for running Python on GPUs and serverless infrastructure. Use when deploying AI/ML models, r... | `skills/modal/SKILL.md`
- **optimize-for-gpu** - GPU-accelerate Python code using CuPy, Numba CUDA, Warp, cuDF, cuML, cuGraph, KvikIO, cuCIM, cuxfilter, cuVS, cuSpati... | `skills/optimize-for-gpu/SKILL.md`

## Cheminformatics & Drug Discovery

- **datamol** - Pythonic wrapper around RDKit with simplified interface and sensible defaults. Preferred for standard drug discovery ... | `skills/datamol/SKILL.md`
- **deepchem** - Molecular ML with diverse featurizers and pre-built datasets. Use for property prediction (ADMET, toxicity) with trad... | `skills/deepchem/SKILL.md`
- **diffdock** - Diffusion-based molecular docking. Predict protein-ligand binding poses from PDB/SMILES, confidence scores, virtual s... | `skills/diffdock/SKILL.md`
- **medchem** - Medicinal chemistry filters. Apply drug-likeness rules (Lipinski, Veber), PAINS filters, structural alerts, complexit... | `skills/medchem/SKILL.md`
- **molfeat** - Molecular featurization for ML (100+ featurizers). ECFP, MACCS, descriptors, pretrained models (ChemBERTa), convert S... | `skills/molfeat/SKILL.md`
- **pytdc** - Therapeutics Data Commons. AI-ready drug discovery datasets (ADME, toxicity, DTI), benchmarks, scaffold splits, molec... | `skills/pytdc/SKILL.md`
- **rdkit** - Cheminformatics toolkit for fine-grained molecular control. SMILES/SDF parsing, descriptors (MW, LogP, TPSA), fingerp... | `skills/rdkit/SKILL.md`
- **rowan** - Rowan is a cloud-native molecular modeling and medicinal-chemistry workflow platform with a Python API. Use for pKa a... | `skills/rowan/SKILL.md`
- **torchdrug** - PyTorch-native graph neural networks for molecules and proteins. Use when building custom GNN architectures for drug ... | `skills/torchdrug/SKILL.md`
- **molecular-dynamics** - Run and analyze molecular dynamics simulations with OpenMM and MDAnalysis. Set up protein/small molecule systems, def... | `skills/molecular-dynamics/SKILL.md`

## Proteomics & Mass Spectrometry

- **matchms** - Spectral similarity and compound identification for metabolomics. Use for comparing mass spectra, computing similarit... | `skills/matchms/SKILL.md`
- **pyopenms** - Complete mass spectrometry analysis platform. Use for proteomics workflows feature detection, peptide identification,... | `skills/pyopenms/SKILL.md`

## Medical Imaging & Digital Pathology

- **histolab** - Lightweight WSI tile extraction and preprocessing. Use for basic slide processing tissue detection, tile extraction, ... | `skills/histolab/SKILL.md`
- **pathml** - Full-featured computational pathology toolkit. Use for advanced WSI analysis including multiplexed immunofluorescence... | `skills/pathml/SKILL.md`
- **pydicom** - Python library for working with DICOM (Digital Imaging and Communications in Medicine) files. Use this skill when rea... | `skills/pydicom/SKILL.md`

## Healthcare AI & Clinical ML

- **neurokit2** - Comprehensive biosignal processing toolkit for analyzing physiological data including ECG, EEG, EDA, RSP, PPG, EMG, a... | `skills/neurokit2/SKILL.md`
- **pyhealth** - Build clinical/healthcare deep-learning pipelines with PyHealth — loading EHR/signal/imaging datasets (MIMIC-III/IV, ... | `skills/pyhealth/SKILL.md`

## Clinical Documentation & Decision Support

- **clinical-decision-support** - Generate professional clinical decision support (CDS) documents for pharmaceutical and clinical research settings, in... | `skills/clinical-decision-support/SKILL.md`
- **clinical-reports** - Write comprehensive clinical reports including case reports (CARE guidelines), diagnostic reports (radiology/patholog... | `skills/clinical-reports/SKILL.md`
- **treatment-plans** - Generate concise (3-4 page), focused medical treatment plans in LaTeX/PDF format for all clinical specialties. Suppor... | `skills/treatment-plans/SKILL.md`

## Neuroscience & Electrophysiology

- **neuropixels-analysis** - Neuropixels neural recording analysis. Load SpikeGLX/OpenEphys data, preprocess, motion correction, Kilosort4 spike s... | `skills/neuropixels-analysis/SKILL.md`

## Protein Engineering & Design

- **adaptyv** - How to use the Adaptyv Bio Foundry API and Python SDK for protein experiment design, submission, and results retrieva... | `skills/adaptyv/SKILL.md`
- **esm** - Comprehensive toolkit for protein language models including ESM3 (generative multimodal protein design across sequenc... | `skills/esm/SKILL.md`
- **glycoengineering** - Analyze and engineer protein glycosylation. Scan sequences for N-glycosylation sequons (N-X-S/T), predict O-glycosyla... | `skills/glycoengineering/SKILL.md`

## Machine Learning & Deep Learning

- **aeon** - This skill should be used for time series machine learning tasks including classification, regression, clustering, fo... | `skills/aeon/SKILL.md`
- **pytorch-lightning** - Deep learning framework (PyTorch Lightning). Organize PyTorch code into LightningModules, configure Trainers for mult... | `skills/pytorch-lightning/SKILL.md`
- **transformers** - This skill should be used when working with pre-trained transformer models for natural language processing, computer ... | `skills/transformers/SKILL.md`
- **stable-baselines3** - Production-ready reinforcement learning algorithms (PPO, SAC, DQN, TD3, DDPG, A2C) with scikit-learn-like API. Use fo... | `skills/stable-baselines3/SKILL.md`
- **pufferlib** - High-performance reinforcement learning framework optimized for speed and scale. Use when you need fast parallel trai... | `skills/pufferlib/SKILL.md`
- **scikit-learn** - Machine learning in Python with scikit-learn. Use when working with supervised learning (classification, regression),... | `skills/scikit-learn/SKILL.md`
- **scikit-survival** - Comprehensive toolkit for survival analysis and time-to-event modeling in Python using scikit-survival. Use this skil... | `skills/scikit-survival/SKILL.md`
- **shap** - Model interpretability and explainability using SHAP (SHapley Additive exPlanations). Use this skill when explaining ... | `skills/shap/SKILL.md`
- **pymc** - Bayesian modeling with PyMC. Build hierarchical models, MCMC (NUTS), variational inference, LOO/WAIC comparison, post... | `skills/pymc/SKILL.md`
- **pymoo** - Multi-objective optimization framework. NSGA-II, NSGA-III, MOEA/D, Pareto fronts, constraint handling, benchmarks (ZD... | `skills/pymoo/SKILL.md`
- **torch-geometric** - Guide for building Graph Neural Networks with PyTorch Geometric (PyG). Use this skill whenever the user asks about gr... | `skills/torch-geometric/SKILL.md`
- **umap-learn** - UMAP dimensionality reduction. Fast nonlinear manifold learning for 2D/3D visualization, clustering preprocessing (HD... | `skills/umap-learn/SKILL.md`
- **statsmodels** - Statistical models library for Python. Use when you need specific model classes (OLS, GLM, mixed models, ARIMA) with ... | `skills/statsmodels/SKILL.md`
- **timesfm-forecasting** - Zero-shot time series forecasting with Google's TimesFM foundation model. Use for any univariate time series (sales, ... | `skills/timesfm-forecasting/SKILL.md`

## Materials Science & Chemistry

- **pymatgen** - Materials science toolkit. Crystal structures (CIF, POSCAR), phase diagrams, band structure, DOS, Materials Project i... | `skills/pymatgen/SKILL.md`
- **cobrapy** - Constraint-based metabolic modeling (COBRA). FBA, FVA, gene knockouts, flux sampling, SBML models, for systems biolog... | `skills/cobrapy/SKILL.md`
- **astropy** - Comprehensive Python library for astronomy and astrophysics. This skill should be used when working with astronomical... | `skills/astropy/SKILL.md`
- **cirq** - Google quantum computing framework. Use when targeting Google Quantum AI hardware, designing noise-aware circuits, or... | `skills/cirq/SKILL.md`
- **pennylane** - Hardware-agnostic quantum ML framework with automatic differentiation. Use when training quantum circuits via gradien... | `skills/pennylane/SKILL.md`
- **qiskit** - IBM quantum computing framework. Use when targeting IBM Quantum hardware, working with Qiskit Runtime for production ... | `skills/qiskit/SKILL.md`
- **qutip** - Quantum physics simulation library for open quantum systems. Use when studying master equations, Lindblad dynamics, d... | `skills/qutip/SKILL.md`

## Engineering & Simulation

- **matlab** - MATLAB and GNU Octave numerical computing for matrix operations, data analysis, visualization, and scientific computi... | `skills/matlab/SKILL.md`
- **fluidsim** - Framework for computational fluid dynamics simulations using Python. Use when running fluid dynamics simulations incl... | `skills/fluidsim/SKILL.md`
- **simpy** - Process-based discrete-event simulation framework in Python. Use this skill when building simulations of systems with... | `skills/simpy/SKILL.md`
- **sympy** - Use this skill when working with symbolic mathematics in Python. This skill should be used for symbolic computation t... | `skills/sympy/SKILL.md`

## Data Analysis & Visualization

- **matplotlib** - Low-level plotting library for full customization. Use when you need fine-grained control over every plot element, cr... | `skills/matplotlib/SKILL.md`
- **seaborn** - Statistical visualization with pandas integration. Use for quick exploration of distributions, relationships, and cat... | `skills/seaborn/SKILL.md`
- **scientific-visualization** - Meta-skill for publication-ready figures. Use when creating journal submission figures requiring multi-panel layouts,... | `skills/scientific-visualization/SKILL.md`
- **geopandas** - Python library for working with geospatial vector data including shapefiles, GeoJSON, and GeoPackage files. Use when ... | `skills/geopandas/SKILL.md`
- **geomaster** - Comprehensive geospatial science skill covering remote sensing, GIS, spatial analysis, machine learning for earth obs... | `skills/geomaster/SKILL.md`
- **dask** - Distributed computing for larger-than-RAM pandas/NumPy workflows. Use when you need to scale existing pandas/NumPy co... | `skills/dask/SKILL.md`
- **polars** - Fast in-memory DataFrame library for datasets that fit in RAM. Use when pandas is too slow but data still fits in mem... | `skills/polars/SKILL.md`
- **vaex** - Use this skill for processing and analyzing large tabular datasets (billions of rows) that exceed available RAM. Vaex... | `skills/vaex/SKILL.md`
- **networkx** - Comprehensive toolkit for creating, analyzing, and visualizing complex networks and graphs in Python. Use when workin... | `skills/networkx/SKILL.md`
- **exploratory-data-analysis** - Perform comprehensive exploratory data analysis on scientific data files across 200+ file formats. This skill should ... | `skills/exploratory-data-analysis/SKILL.md`
- **statistical-analysis** - Guided statistical analysis with test selection and reporting. Use when you need help choosing appropriate tests for ... | `skills/statistical-analysis/SKILL.md`

## Document Processing

- **pdf** - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables... | `skills/pdf/SKILL.md`
- **docx** - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers in... | `skills/docx/SKILL.md`
- **xlsx** - Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants t... | `skills/xlsx/SKILL.md`
- **pptx** - Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slid... | `skills/pptx/SKILL.md`
- **markitdown** - Convert files and office documents to Markdown. Supports PDF, DOCX, PPTX, XLSX, images (with OCR), audio (with transc... | `skills/markitdown/SKILL.md`

## Scientific Communication & Publishing

- **paper-lookup** - Search 10 academic paper databases via REST APIs for research papers, preprints, and scholarly articles. Covers PubMe... | `skills/paper-lookup/SKILL.md`
- **bgpt-paper-search** - Search scientific papers and retrieve structured experimental data extracted from full-text studies via the BGPT MCP ... | `skills/bgpt-paper-search/SKILL.md`
- **literature-review** - Conduct comprehensive, systematic literature reviews using multiple academic databases (PubMed, arXiv, bioRxiv, Seman... | `skills/literature-review/SKILL.md`
- **scientific-writing** - Core skill for the deep research and writing tool. Write scientific manuscripts in full paragraphs (never bullet poin... | `skills/scientific-writing/SKILL.md`
- **peer-review** - Structured manuscript/grant review with checklist-based evaluation. Use when writing formal peer reviews with specifi... | `skills/peer-review/SKILL.md`
- **citation-management** - Comprehensive citation management for academic research. Search Google Scholar and PubMed for papers, extract accurat... | `skills/citation-management/SKILL.md`
- **pyzotero** - Interact with Zotero reference management libraries using the pyzotero Python client. Retrieve, create, update, and d... | `skills/pyzotero/SKILL.md`
- **scientific-slides** - Build slide decks and presentations for research talks. Use this for making PowerPoint slides, conference presentatio... | `skills/scientific-slides/SKILL.md`
- **latex-posters** - Create professional research posters in LaTeX using beamerposter, tikzposter, or baposter. Support for conference pre... | `skills/latex-posters/SKILL.md`
- **pptx-posters** - Create research posters using HTML/CSS that can be exported to PDF or PPTX. Use this skill ONLY when the user explici... | `skills/pptx-posters/SKILL.md`
- **venue-templates** - Access comprehensive LaTeX templates, formatting requirements, and submission guidelines for major scientific publica... | `skills/venue-templates/SKILL.md`
- **paper-2-web** - This skill should be used when converting academic papers into promotional and presentation formats including interac... | `skills/paper-2-web/SKILL.md`
- **scientific-schematics** - Create publication-quality scientific diagrams using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.... | `skills/scientific-schematics/SKILL.md`
- **infographics** - Create professional infographics using Nano Banana Pro AI with smart iterative refinement. Uses Gemini 3 Pro for qual... | `skills/infographics/SKILL.md`
- **markdown-mermaid-writing** - Comprehensive markdown and Mermaid diagram writing skill. Use when creating any scientific document, report, analysis... | `skills/markdown-mermaid-writing/SKILL.md`
- **generate-image** - Generate or edit images using AI models (FLUX, Nano Banana 2). Use for general-purpose image generation including pho... | `skills/generate-image/SKILL.md`

## Research Methodology & Planning

- **hypothesis-generation** - Structured hypothesis formulation from observations. Use when you have experimental observations or data and need to ... | `skills/hypothesis-generation/SKILL.md`
- **scientific-brainstorming** - Creative research ideation and exploration. Use for open-ended brainstorming sessions, exploring interdisciplinary co... | `skills/scientific-brainstorming/SKILL.md`
- **scientific-critical-thinking** - Evaluate scientific claims and evidence quality. Use for assessing experimental design validity, identifying biases a... | `skills/scientific-critical-thinking/SKILL.md`
- **scholar-evaluation** - Systematically evaluate scholarly work using the ScholarEval framework, providing structured assessment across resear... | `skills/scholar-evaluation/SKILL.md`
- **what-if-oracle** - Run structured What-If scenario analysis with multi-branch possibility exploration. Use this skill when the user asks... | `skills/what-if-oracle/SKILL.md`
- **consciousness-council** - Run a multi-perspective Mind Council deliberation on any question, decision, or creative challenge. Use this skill wh... | `skills/consciousness-council/SKILL.md`
- **dhdna-profiler** - Extract cognitive patterns and thinking fingerprints from any text. Use this skill when the user wants to analyze how... | `skills/dhdna-profiler/SKILL.md`
- **research-grants** - Write competitive research proposals for NSF, NIH, DOE, DARPA, and Taiwan NSTC. Agency-specific formatting, review cr... | `skills/research-grants/SKILL.md`
- **research-lookup** -  | `skills/research-lookup/SKILL.md`
- **market-research-reports** - Generate comprehensive market research reports (50+ pages) in the style of top consulting firms (McKinsey, BCG, Gartn... | `skills/market-research-reports/SKILL.md`
- **paperzilla** - Chat with your agent about projects, recommendations, and canonical papers in Paperzilla. Use when users ask for rece... | `skills/paperzilla/SKILL.md`
- **parallel-web** - All-in-one web toolkit powered by parallel-cli, with a strong emphasis on academic and scientific sources. Use this s... | `skills/parallel-web/SKILL.md`

## Laboratory Automation

- **pylabrobot** - Vendor-agnostic lab automation framework. Use when controlling multiple equipment types (Hamilton, Tecan, Opentrons, ... | `skills/pylabrobot/SKILL.md`

## Multi-omics & Systems Biology

- **hypogenic** - Automated LLM-driven hypothesis generation and testing on tabular datasets. Use when you want to systematically explo... | `skills/hypogenic/SKILL.md`

## Regulatory & Standards

- **iso-13485-certification** - Comprehensive toolkit for preparing ISO 13485 certification documentation for medical device Quality Management Syste... | `skills/iso-13485-certification/SKILL.md`

## Infrastructure & Resources

- **get-available-resources** - This skill should be used at the start of any computationally intensive scientific task to detect and report availabl... | `skills/get-available-resources/SKILL.md`

## Meta & Agent Tools

- **autoskill** - Observe the user's screen via screenpipe, detect repeated research workflows, match them against existing scientific-... | `skills/autoskill/SKILL.md`