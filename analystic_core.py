# Bu dosya egitim verilerinden ogrenme metrikleri cikarmak icin var
quiz_results = [
    {"student_id": 1, "score": 80, "topic": "Loops"},
    {"student_id": 1, "score": 75, "topic": "Functions"},
    {"student_id": 1, "score": 90, "topic": "Lists"},
    {"student_id": 2, "score": 85, "topic": "Loops"},
    {"student_id": 2, "score": 70, "topic": "Functions"},
    {"student_id": 2, "score": 95, "topic": "Lists"},
    {"student_id": 3, "score": 78, "topic": "Loops"},
    {"student_id": 3, "score": 82, "topic": "Functions"},
    {"student_id": 3, "score": 92, "topic": "Lists"}
]
def calculate_average_score(quiz_results):
    """
    Amac: Ogrencilerin genel basari seviyesini olcmek.
    Bu metrik sinifin genel durumunu hizlica gormek icin kullanilir.
    """
    # Her ogrencinin skorlarini grupla
    student_scores = {}
    for result in quiz_results:
        student_id = result["student_id"]
        if student_id not in student_scores:
            student_scores[student_id] = []
        student_scores[student_id].append(result["score"])
    
    # Her ogrencinin ortalamasini hesapla
    student_averages = [sum(scores) / len(scores) for scores in student_scores.values()]
    
    # Genel ortalamayi hesapla
    average_score = sum(student_averages) / len(student_averages)
    return average_score
print(calculate_average_score(quiz_results))


def find_topic_weakness(quiz_results):
    """
    Amac: Konu bazli zayiflik analizi yapmak
    Tanim:
    Konu ortalamasi ne kadar dusuk ise o konuda zayiflik var.

    Donen deger: 
    [("topic", average_score), ......] en zayiftan en gucluye sirali liste
    """
    topic_scores = {}

    #Topic bazinda skorlari grupla 

    for result in quiz_results:
        topic = result["topic"]
        score = result["score"]

        if topic not in topic_scores:
            topic_scores[topic] = []
        topic_scores[topic].append(score)

    # Topic ortalamalarini hespala
    topic_averages = []
    for topic, scores in topic_scores.items():
        avg = sum(scores) / len(scores)
        topic_averages.append((topic, avg))

    # En zayiftan en gucluya sirala
    topic_averages.sort(key=lambda x: x[1])

    return topic_averages


def calculate_progress_trend(quiz_results):
    """
    Amac: Zaman icinde ogrenme ilerlemesini analiz etmek
    """
    pass 
print(find_topic_weakness(quiz_results))
