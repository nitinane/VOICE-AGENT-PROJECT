# 🏦 Union Bank of India: AI Smart Kiosk (Powered by KAI)

A high-fidelity, dual-purpose AI banking solution designed for both **Self-Service Kiosks** and **Frontline Staff Assistance**. This project leverages state-of-the-art LLMs and Voice AI to bridge the language gap in banking, specifically tailored for the diverse linguistic landscape of India.

---

## 🌟 Overview

The **Union Bank AI Smart Kiosk** (KAI) is an Operating System for modern banking. It provides a seamless, voice-first experience for customers in rural and urban areas, while simultaneously empowering branch staff with a real-time "Co-pilot" for multilingual support.

- **Vision**: To make banking accessible to everyone, regardless of language preference or technical literacy.
- **Core Intelligence**: Powered by **Llama-3.3 70B** for deterministic banking logic and **Murf AI** for natural, human-like voice synthesis.


### 👤 Customer Login (Kiosk)
- **Account Number**: `510101234567890`
- **Password**: `union@123`
- **Transaction PIN**: `1234`
- **Demo User**: `Ravi Kumar`

### 🛡️ Staff Login (Assist)
- **Staff ID**: `staff001`
- **Password**: `bank123`

---

## 🚀 Key Modules

### 1. 🖥️ Self-Service Kiosk (Customer Facing)
A voice-activated terminal that allows customers to perform core banking tasks without human intervention.
- **Services**: Balance inquiry, cash withdrawal simulation, fund transfers, and instant KYC updates.
- **Voice-First**: Fully navigable via speech, with a high-fidelity "Money Moment" simulation.
- **Multilingual Support**: English, Hindi, Telugu, Tamil, Kannada, and Malayalam.

### 2. 🛡️ Frontline Assist (Staff Co-pilot)
A specialized dashboard for branch staff to manage regional interactions.
- **Real-time Translation**: Bridges the gap between staff (English/Hindi) and regional customers.
- **Process Guidance**: Dynamic SOP reminders and eligibility checks for complex tasks like account opening or loans.
- **CRM Integration**: Automatic session summaries exported to simulated CRM for audit and compliance.

---

## 🛠️ Technical Stack

- **Framework**: [Next.js 15+](https://nextjs.org/) (App Router)
- **UI/UX**: [Tailwind CSS](https://tailwindcss.com/) & [Framer Motion](https://www.framer.com/motion/) for premium glassmorphic design.
- **AI Engine**: [Groq Cloud](https://groq.com/) (Llama-3.3 70B) for ultra-low latency inference.
- **Voice Orchestration**: [Murf AI](https://murf.ai/) for high-quality regional TTS.
- **Streaming**: [LiveKit](https://livekit.io/) for real-time interaction and voice state management.
- **State Management**: [Zustand](https://zustand-demo.pmnd.rs/) for robust, lightweight global state.

---

## 📂 Project Highlights

- **`src/app/kiosk`**: High-fidelity terminal UI with integrated voice interaction hooks.
- **`src/app/staff`**: Cognitive staff dashboard with live transcription and intent detection.
- **`src/i18n/translations.ts`**: Massive localized dictionary covering all banking intents and UI labels.
- **`src/hooks/useVoiceInteraction.ts`**: The core bridge between STT, LLM inference, and TTS playback.

---

## ⚙️ Setup & Installation

1. **Clone & Install**:
   ```bash
   npm install
   ```

2. **Environment Configuration**:
   Create a `.env.local` file based on `.env.example`:
   ```env
   GROQ_API_KEY=your_groq_key
   MURF_API_KEY=your_murf_key
   # Local testing credentials provided in .env.example
   ```

3. **Run Dev Environment**:
   ```bash
   npm run dev
   ```
   Open [http://localhost:3000](http://localhost:3000) to see the result.

---

## 🔐 Credentials (Demo Simulation)

For evaluation and testing, please use the following synthetic credentials:

---

## ✨ Features Checklist
- [x] **Global Multilingual Enforcement**: AI speaks the user's selected language consistently.
- [x] **Glassmorphic UI**: Premium, modern interface with Union Bank branding.
- [x] **Interactive Dialpad**: Numeric simulation for secure PIN and account entry.
- [x] **Audit Ready**: Every voice session generates a structured summary for CRM.
- [x] **Low Latency**: Optimized inference path for near-human response times.

---
*© 2025 Union Bank of India — AI Innovation Lab*
