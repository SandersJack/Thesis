# 📘 Kaon Identification Upgrade and Search for the Dark Photon Production in the π⁰ → γ A′ Decay, at NA62

This repository contains the full source code and LaTeX files associated with the thesis.

## 🧾 Abstract

The 2022--2024 data from the NA62 experiment at CERN has been used to search for dark photon (A′) production in the `π⁰ → A′γ` decay, and subsequent prompt decay `A′ → e⁺e⁻`. Within the mass range `6 ≤ m_A′ ≤ 121.6 MeV/c²`, no signal is observed and an exclusion limit on the mixing parameter `ε²` across the mass range is obtained.

The NA62 beam consists of 6% kaons, therefore requiring beam particle identification conducted by the KTAG. The KTAG comprises a CEDAR and a purpose-built photon-detection system. Since 2016, NA62 has employed a CEDAR with a nitrogen radiator gas. To reduce the amount of material in the beam's path, a new CEDAR utilising hydrogen (H₂) as a radiator has been used since 2023. The CH detector design, testing and commissioning at NA62 are presented. The CEDAR with H₂ achieved a kaon identification efficiency of 99.7% and a kaon time resolution of 66 ps.

Finally, software developments towards the design of the High Intensity Kaon Experiments (HIKE) facility are presented.

---

## 📂 Repository Structure

```plaintext
.
├── analysis/                # Analysis files for word count workflow
├── data/                    # Processed latex files
├── Chapters/                # LaTeX files for each chapters
├── Scripts /                # Number of utility scripts used in latex building and git workflows
├── acronyms.tex             # List of acronyms within the document
├── final_submission.pdf     # Final submission pdf <--- READ THIS 
├── iopart-num.bst           # Reference style sued in latex
├── main.tex                 # Main latex file
├── README.md                # This file
└── references.bib           # Bibliography file