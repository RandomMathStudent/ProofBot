# Initial thoughts
Image
  ↓

Vision Model
  ↓

Structured Mathematical Document
  ↓

Mathematical Understanding Layer
  ↓

Lean Formalization Agent
  ↓

Lean Compiler Feedback
  ↓

Repair Agent
  ↓

Verified Lean Code



https://github.com/datalab-to/marker

https://github.com/facebookresearch/nougat

https://github.com/lukas-blecher/LaTeX-OCR





Handwritten Proof
        │
        ▼
Image Preprocessing
        │
        ▼
Layout & Region Detection
        │
        ├───────────────┐
        ▼               ▼
Handwriting OCR     Formula Recognition
        │               │
        └──────┬────────┘
               ▼
      Structured Proof AST
               ▼
      Proof Relationship Extraction
               ▼
      Autoformalization LLM
               ▼
      Lean Code Generation
               ▼
      Lean Verification
               ▼
      Error Localization
               ▼
 User Feedback on Original Image