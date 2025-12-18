# EyeScribe  
### Vision-Based Assistive Gaze Communication Interface

EyeScribe is a **vision-based assistive Human–Computer Interaction (HCI) system** that enables hands-free computer interaction using **eye gaze captured through a standard webcam**. The system is designed for individuals with severe motor impairments who are unable to use traditional input devices such as keyboards and mice.

By eliminating the need for proprietary infrared eye-tracking hardware, EyeScribe provides a **cost-effective, hardware-agnostic, and accessible** solution for digital communication.

---

## Problem Statement

Individuals affected by conditions such as **Amyotrophic Lateral Sclerosis (ALS)**, **Cerebral Palsy**, and **Spinal Cord Injuries** often lose voluntary motor control while retaining eye movement. Existing gaze-based assistive technologies rely on specialized infrared sensors, making them expensive, non-portable, and inaccessible to many users.

There is a need for a **software-only gaze interaction system** that is affordable, stable, and usable in real-world environments.

---

## Proposed Solution

EyeScribe addresses this problem by utilizing:

- Standard consumer-grade webcams for video capture  
- Pre-trained computer vision models for facial and eye landmark detection  
- Personalized calibration using regression-based mapping  
- Signal smoothing techniques to reduce gaze jitter  
- Gaze-driven interaction methods suitable for assistive use  

The system allows users to **navigate, select, and communicate** using only eye movements.

---

## System Architecture

The EyeScribe pipeline consists of the following stages:

1. **Video Acquisition**  
   Real-time video capture from a standard webcam.

2. **Facial Landmark Detection**  
   A pre-trained CNN-based model (MediaPipe Face Mesh) detects facial and ocular landmarks.

3. **Gaze Calibration**  
   A supervised regression model maps eye coordinates to screen coordinates, personalized for each user.

4. **Signal Smoothing**  
   Kalman Filtering or Weighted Moving Average techniques are applied to reduce noise and micro-saccadic jitter.

5. **Interaction Layer**  
   Cursor movement is controlled through gaze direction, with selection performed using dwell-time or blink detection.

---

## Key Features

- Webcam-based gaze tracking (no infrared hardware required)
- Personalized user calibration
- Smooth and stable cursor control
- Dwell-time and blink-based interaction
- Fully on-device processing for privacy
- Suitable for assistive communication scenarios

---

## Technology Stack

| Component | Technology |
|---------|------------|
| Programming Language | Python 3.9+ |
| Computer Vision | OpenCV |
| Facial Landmark Detection | MediaPipe Face Mesh |
| Machine Learning | Scikit-learn (Regression) |
| Signal Processing | Kalman Filter |
| System Control | PyAutoGUI |
| Numerical Computing | NumPy |

---

## Data Usage

EyeScribe does not rely on a fixed external dataset.

- Operates on live webcam video streams  
- Generates a small, user-specific calibration dataset during setup  
- No video or biometric data is stored or transmitted  

This approach enhances personalization while preserving user privacy.

---

## Intended Users

- Individuals with severe motor impairments  
- Rehabilitation and assistive technology centers  
- Accessibility researchers and HCI practitioners  

---

## Evaluation Criteria

System performance is evaluated based on:

- Cursor stability and smoothness  
- Responsiveness to gaze input  
- Usability for hands-free interaction  
- Reduction of jitter compared to raw gaze mapping  

---

## Future Work

- On-screen keyboard with predictive text
- Text-to-speech integration
- Improved adaptive smoothing mechanisms
- Multi-monitor and mobile platform support

---

## References

- Go et al., *MoMa: An Assistive Mobile Manipulator with a Webcam-Based Gaze Control System*, HardwareX, Elsevier, 2024  
- Athar et al., *AI-Assisted Cursor Navigation Using Eye Gaze Detection*, 2025  
- Rao et al., *Facial Landmark Stabilization Using Optical Flow*, 2023  

---

## Academic Context

This project was developed as part of a **Master of Computer Applications (MCA) Main Project**, focusing on **Assistive Technologies, Computer Vision, and Human–Computer Interaction**.

---

## License

This project is intended for **academic and research use only**.
