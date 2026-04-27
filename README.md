## 🚀 Método Bremerton / Semantic Contextualizer

AI-powered NLP assistant designed to reduce cognitive latency in specialized English learning (IELTS-focused), using local AI models for technological autonomy.

---

## 🌍 Problem

* El inglés tiene más de 1.4 mil millones de hablantes
* El aprendizaje de inglés técnico (ej: *The Economist*) genera:

  * Alta latencia cognitiva
  * Bajo nivel de retención contextual
* Dependencia de APIs → costos por tokens + latencia

---

## 💡 Solution

Un asistente NLP que:

* Interpreta palabras en contexto (no aisladas)
* Genera significado pragmático + visual
* Reduce tiempo de comprensión
* Funciona con modelos locales (offline-first)

---

## 🧠 Methodology

Basado en Design Thinking:

* Empathize → estudiantes IELTS
* Define → latencia cognitiva
* Ideate → contextualización semántica
* Prototype → LLM + interfaz
* Test → iteración con usuarios

---

## ⚙️ Functional Design

### Phase 1 – Semantic Core

**Input**

* Keyword + short context (<20 words)

**Processing**

* Inferencia semántica vía LLM

**Output**

* Word DNA:

  * Pronunciación (IPA)
  * Significado pragmático
* “The Vibe”:

  * Analogía visual para fijación
* Token counter:

  * Control de costos

---

### Phase 2 – Cognitive Layer

* Mnemonic Web → conexión entre palabras
* Intensity Scale → jerarquía de matices
* IELTS Strategy → aplicación práctica

---

## 🏗️ Architecture

* Frontend: R Shiny
* Orchestration: Python (reticulate)
* AI Engine:

  * Local → Ollama + Llama 3
  * Fallback → Cloud API (Hybrid inference strategy where first Local LLM words offline, if it falls , the arquitecture uses a cloud API based on  hardware or performance constraints)

---

## ⚠️ Constraints

* Intel HD 5500
* 8 GB RAM
* ~1.7 GB usable

---

## 🎯 Strategy

* Desarrollo modular (MVP)
* Enfoque en:

  * Baja latencia
  * Independencia tecnológica
  * Escalabilidad sin costo por token

---

## 🔮 Vision

* Asistente autónomo de aprendizaje
* Reducción radical del tiempo de comprensión
* Sistema adaptable por dominio

---

## Demo

Streamlit interface:
👉 [[Link a tu app](https://nlp-english-learning-assistant-druqfucyyzvonf3xczu6hm.streamlit.app/)]
