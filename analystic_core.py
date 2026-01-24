import json
from datetime import datetime

def parse_dt(dt_str: str) -> datetime:
    return datetime.fromisoformat(dt_str)


# Bu dosya egitim verilerinden ogrenme metrikleri cikarmak icin var
quiz_results = [
    {"student_id": 1, "created_at": "2026-01-15T10:00:00", "score": 80, "topic": "Loops"},
    {"student_id": 1, "created_at": "2026-01-15T11:00:00", "score": 75, "topic": "Functions"},
    {"student_id": 1, "created_at": "2026-01-15T12:00:00", "score": 90, "topic": "Lists"},

    {"student_id": 2, "created_at": "2026-01-15T11:00:00", "score": 85, "topic": "Loops"},
    {"student_id": 2, "created_at": "2026-01-15T12:00:00", "score": 70, "topic": "Functions"},
    {"student_id": 2, "created_at": "2026-01-15T13:00:00", "score": 95, "topic": "Lists"},

    {"student_id": 3, "created_at": "2026-02-15T11:00:00", "score": 78, "topic": "Loops"},
    {"student_id": 3, "created_at": "2026-02-15T12:00:00", "score": 82, "topic": "Functions"},
    {"student_id": 3, "created_at": "2026-02-15T13:00:00", "score": 92, "topic": "Lists"},
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


def find_topic_weakness(quiz_results):
    """
    Amac: Konu bazli zayiflik analizi yapmak
    Tanim:
    Konu ortalamasi ne kadar dusuk ise o konuda zayiflik var.

    Donen deger:
    [("topic", average_score), ......] en zayiftan en gucluye sirali liste
    """
    topic_scores = {}

    # Topic bazinda skorlari grupla
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

    # En zayiftan en gucluye sirala
    topic_averages.sort(key=lambda x: x[1])

    return topic_averages

    # Not:
    # Topic weakness olcumunu ortalama ile yaptik.
    # İleride median / dusuk skor orani gibi metriklerle daha saglam hale getirilebilir.


def calculate_topic_progress_trend(quiz_results):
    """
    Amac: Ogrencilerin kon bazli gelisimini analiz etmek
    Cikti: {student_id: {topic: {"start": x, "end": y, "delta": y-x}}}
    """
    grouped = {}
    for r in quiz_results:
        sid = r["student_id"]
        topic = r["topic"]
        grouped.setdefault(sid, {})
        grouped[sid].setdefault(topic, [])
        grouped[sid][topic].append(r)

    trends = {}

    # 2) Her ogrenci ve topic icin created_at'e gore sirala, start/end cikar
    for sid, topics_dict in grouped.items():
        trends[sid] = {}

        for topic, records in topics_dict.items():
            records_sorted = sorted(records, key=lambda x: parse_dt(x["created_at"]))

            start = records_sorted[0]["score"]
            end = records_sorted[-1]["score"]

            trends[sid][topic] = {
                "start": start,
                "end": end,
                "delta": end - start
            }

    return trends

def generate_summary_report(quiz_results):
    """
    Amac: Hesaplanan metrikleri tek bir rapor objesinde toplamak.
    Not: Bu fonksiyon print etmez; veri döndürür. (API/JSON için ideal)
    """
    avg = calculate_average_score(quiz_results)
    weaknesses = find_topic_weakness(quiz_results)
    trends = calculate_topic_progress_trend(quiz_results)

    # weaknesses tuple list -> dict list
    weaknesses_json = [{"topic": topic, "avg_score": round(score, 2)} for topic, score in weaknesses]

    # trends dict zaten JSON'a uygun ama değerleri netleştirelim
    return {
        "class_average_score": round(avg, 2),
        "weak_topics": weaknesses_json,
        "topic_trends": trends
    }

def save_report_to_json(report, filepath="report.json"):
    """
    Amac: Raporu JSON dosyasi olarak kaydetmek.
    ensure_ascii=False -> Türkçe karakterleri bozmadan yazar.
    indent=2 -> okunabilir format.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def print_summary_report(quiz_results):
    avg = calculate_average_score(quiz_results)
    weaknesses = find_topic_weakness(quiz_results)
    trends = calculate_topic_progress_trend(quiz_results)

    print("\n" + "=" * 40)
    print("LEARNING ANALYTICS SUMMARY REPORT")
    print("=" * 40)

    print(f"\nClass average score (student-weighted): {avg:.2f}")

    print("\nWeak topics (low -> high):")
    for topic, score in weaknesses:
        print(f"  - {topic}: {score:.2f}")

    print("\nTopic trends by student (showing non-zero deltas):")
    any_change = False
    for sid, topics in trends.items():
        for topic, t in topics.items():
            if t["delta"] != 0:
                any_change = True
                print(f"  - Student {sid} | {topic}: start={t['start']} end={t['end']} delta={t['delta']}")

    if not any_change:
        print("  (No trend changes yet — need multiple records per topic.)")

    print("\nTip: To see trend, add more records for the SAME student + SAME topic over time.")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    # Trend'i görünür yapmak için öğrenci 1 - Loops'a 2 yeni kayıt ekleyelim
    quiz_results.append({"student_id": 1, "created_at": "2026-01-15T14:00:00", "score": 88, "topic": "Loops"})
    quiz_results.append({"student_id": 1, "created_at": "2026-01-15T15:00:00", "score": 92, "topic": "Loops"})
    
    print(calculate_average_score(quiz_results))
    print(find_topic_weakness(quiz_results))

    topic_trends = calculate_topic_progress_trend(quiz_results)
    print(topic_trends)
    print(topic_trends[1]["Loops"])

    report = generate_summary_report(quiz_results)
    save_report_to_json(report)
    print("Saved report to report.json")

    # Daha okunakli rapor:
    print_summary_report(quiz_results)
