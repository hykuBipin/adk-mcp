# Submission Evidence: ADK Context Filtration

This folder contains screenshot evidence demonstrating the successful implementation of prompt context filtration in our ADK Location Intelligence Agent.
<img width="1710" height="1078" alt="image" src="https://github.com/user-attachments/assets/8ca1f776-4f32-497d-b197-e437802fa5ea" />

## 1. When ADK doesn't restrict with context filtering
*(The agent mistakenly answers out-of-bounds questions like "Who is current CM of TamilNadu 2026?" instead of rejecting them.)*

<img width="1710" height="1088" alt="Screenshot 2026-05-09 at 3 38 26 PM" src="https://github.com/user-attachments/assets/876d7948-9ee1-4fcf-ab5f-9c6d541f08b8" />
<img width="1710" height="1064" alt="Screenshot 2026-05-09 at 3 39 44 PM" src="https://github.com/user-attachments/assets/604e127f-e451-46d2-8a23-f4c969a23975" />
<img width="1710" height="1097" alt="Screenshot 2026-05-09 at 3 40 03 PM" src="https://github.com/user-attachments/assets/f3de7bbe-0d22-4c37-b967-69f96bedb488" />
<img width="1710" height="1093" alt="Screenshot 2026-05-09 at 3 41 09 PM" src="https://github.com/user-attachments/assets/9ef8823a-65a0-4a28-b472-4bd568fd9e73" />



## 2. When ADK has the ability to filter the prompt
*(The agent successfully intercepts the out-of-bounds prompt and throws the generic exception: "question asked in prompt is out of our context." as instructed in `agent.py`.)*

<img width="1710" height="1075" alt="Screenshot 2026-05-09 at 5 21 31 PM" src="https://github.com/user-attachments/assets/f620fd55-7e6c-4844-b94b-eb3c8cfb607d" />
<img width="1710" height="1107" alt="Screenshot 2026-05-09 at 5 22 02 PM" src="https://github.com/user-attachments/assets/482f198e-a1ba-4f60-9236-c8e28076b7c5" />
