import csv
import json

# gpu jsonl 변환 amd, intel, nvidia
# power jsonl 변환


# JSONL 파일에 저장할 데이터 형식을 정의합니다.
data = []

# CSV 파일에서 데이터를 읽어와 JSONL 파일에 저장합니다.
with open('data/power.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 헤더를 건너뜁니다.
    for row in reader:
        # 각 행마다 message 리스트를 감싸는 딕셔너리를 생성합니다.
        message_data = {
            "messages": [
                # 첫 번째 메시지: 시스템 메시지
                {
                    "role": "system",
                    "content": "Your chatbot is a factual chatbot that is also sarcastic."
                },
                # 두 번째 메시지: 사용자 메시지
                {
                    "role": "user",
                    "content": row[0] + "에 대해 설명해줘"
                },
                # 세 번째 메시지: 어시스턴트 메시지
                {
                    "role": "assistant",
                    "content": row[1]
                }
            ]
        }
        data.append(message_data)

# JSONL 파일에 데이터를 씁니다.
with open('dataset/power.jsonl', 'w', encoding='utf-8') as jsonlfile:
    for message_data in data:
        json.dump(message_data, jsonlfile, ensure_ascii=False)
        jsonlfile.write('\n')
