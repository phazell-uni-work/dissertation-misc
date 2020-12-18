def nmsSpan(n,qu):
    num = n
    q = qu
    print(f"<span>\n<p>{num} - {q}</p>\n<input type=\"radio\" id=\"t{num}\" name=\"nms{num}\" value=\"true\">\n<label for=\"true\">true</label>\n<input type=\"radio\" id=\"f{num}\" name=\"nms{num}\" value=\"false\">\n<label for=\"false\">false</label><br>\n</span><br /><br />")


qdic = {
    "Dribbling during the daytime":1,
    "Loss of taste or smell":2,
    "Difficulty swallowing food":3,
    "Vomitting or feeling of sickness":4,
    "Constipation":5,
    "Bowel incontinence":6,
    "Feeling your bowel emptying is incomplete":7,
    "A sense of urgency to pass urine":8,
    "Getting up regularly to pass urine at night":9,
    "Unexplained pains":10,
    "Unexplained change in weight":11,
    "Problem remembering things..":12,
    "Loss of interest ...":13,
    "Seeing or hearing things that you are know/told are not there":14,
    "Difficulty concentrating":15,
    "Feeling sad/blue":16,
    "Feeling anxious or panicky":17,
    "Feeling less interested in sex":18,
    "Finding it difficult to have sex":19,
    "Feeling light headed, dizzy or weak":20,
    "Falling":21,
    "Finding it difficult to stay awake during activities":22,
    "Difficulty going to sleep":23,
    "Intense vivid dreams":24,
    "Talking or moving about in your sleep":25,
    "Unpleasant sensations in your legs":26,
    "Swelling of your legs":27,
    "Excessive sweating":28,
    "Double vision":29,
    "Believing things are happening to you that other people say aren' true":30,
    "Increase in thoughts... more medicine than prescribed":31,
}

# for a,b in qdic.items():
#     nmsSpan(b,a)

def lazygo(a):
    x = a
    y = f"pdq_c_{a} integer,\n"
    return y

out = ""
for b in range(1,30):
    out += lazygo(b)

print(out)