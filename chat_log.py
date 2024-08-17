import os
import json

class ChatLog:
    def __init__(self, max_length = 10):
        self.chat_history = []
        self.max_length = max_length

    def add_to_log(self, user_input, llm_response):
        self.chat_history.append({"user": user_input, "llm": llm_response})
        
        # 대화 기록이 max_length>10 이면 log delete
        if len(self.chat_history) > self.max_length:
            self.chat_history.pop(0)

    def get_log(self):
        return self.chat_history

    def clear_log(self):
        self.chat_history = []

    def save_log_to_file(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.chat_history, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"저장 중 오류 발생: {e}")

    def load_log_from_file(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    self.chat_history = json.load(file)
            else:
                print(f"파일 {filename}을 찾을 수 없습니다.")
        except Exception as e:
            print(f"불러오기 중 오류 발생: {e}")