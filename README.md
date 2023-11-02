# Information Extraction for Legal Wills

This repository contains the corpus and code for the paper "Information Extraction from Legal Wills: How Well Does GPT-4 Do?" (To appear in the Findings of the Association for Computational Linguistics: EMNLP 2023).

## About The Project

This project introduces a manually annotated dataset for IE from legal wills. Our dataset consists of 16,018 annotations of entities, relations, and events extracted from 45 legal wills from two US states: Tennessee and Idaho. You can find detailed explanation of the information types extracted in our dataset in Appendix B of [our paper](https://clulab.org/papers/emnlp2023_kwak-et-al.pdf).

We evaluated GPT-4 with in-context learning on our dataset, in both in-domain (i.e., examples from the same state) and out-of-domain (OOD) (i.e., examples from another state) settings. The evaluation results demonstrate that GPT-4 is capable of handling the legal information extraction task in this in-context-learning setting. However, GPT-4 is not perfect: we observed inconsistent outputs (given a prompt) as well as prompt over-generalization. For more details, please see our paper [here](https://clulab.org/papers/emnlp2023_kwak-et-al.pdf).

## Usage
### Dataset

Our dataset can be used to evaluate large language models on a legal IE task. The raw datasets contain full entities, relations, and events which amount to 16,018 annotations. The datasets used for the LLM evaluation for our project contains four most common entities (i.e., testator, beneficiary, asset, will) and four most common relations (testator-beneficiary, testator-asset, beneficiary-asset, testator-will) only. If you'd like to check the full annotations, please see the raw datasets. If you'd like to evaluate LLM on the legal IE, you may refer to our evaluation datasets.

### Codes

#### A code for OCR (PDF to text)

To extract will texts from PDFs, we ran OCR using python libraries (pdf2image, pytesseract).

To run the code, first install the following libraries by running the code below: `pdf2image`, `pytesseract`, `tesseract` 

```
pip install pdf2image pytesseract tesseract
sudo apt-get install poppler-utils
sudo apt install tesseract-ocr && sudo apt install libtesseract-dev
```

Once you are finished with installing the libraries, run `PDF_to_text.py`

#### A code for transforming raw datasets into evaluation datasets (raw to evaluation datasets)

To transform raw datasets into evaluation datasets, run `raw_to_evaluation_datasets.py`

### Prompt

You can find the prompts used for the LLM evaluation in `./docs` (`evaluation_prompt_for_entity.txt`, `evaluation_prompt_for_relation.txt`)

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. See [LICENSE.md](https://github.com/ml4ai/ei4wills/blob/main/LICENSE.md) for more details.

## Contact

If you have any questions or comments on our work, please contact the person below.

Alice Kwak - alicekwak@arizona.edu

## Acknowledgements

We appreciate [Label Studio](https://labelstud.io) for providing access to Label Studio Enterprise Cloud Platform through their Academic Program.
