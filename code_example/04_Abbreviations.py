#-*- coding:utf-8 -*-
# DRY / OAOO

user_math_score_dic = {
    'A': 90,
    'B': 93,
    'C': 30,
    'D': 100,
    'E': 31,
    'F': 82,
    'G': 79,
}

user_eng_score_dic = {
    'A': 30,
    'B': 63,
    'C': 39,
    'D': 94,
    'E': 10,
    'F': 49,
    'G': 68,
}

# Danger code
def get_user_score_list(user_math_score_dic, user_eng_score_dic):
    """
    input: 유저의 이름을 key로, 점수를 value로 가지는 dict형 자료형 2개
    output: 종합 점수 계산에 따라 내림차순으로 정렬한 유저의 이름 list
    """
    
    user_sum_score_dic = {}
    # 종합 점수 계산 (math*2 + eng)
    for k, math_score in user_math_score_dic.items():
        sum_score = math_score*2
        sum_score += user_eng_score_dic[k]
        user_sum_score_dic[k] = sum_score

    # 종합 점수에 따라 내림차순 정렬
    sorted_user = sorted(user_sum_score_dic.keys(), key=lambda x: user_sum_score_dic[x])
    return sorted_user

print("# Danger code")
print(get_user_score_list(user_math_score_dic, user_eng_score_dic))


# Good code
def calc_user_sum_score(user_math_score_dic, user_eng_score_dic):
    """
    input: 유저의 이름을 key로, 점수를 value로 가지는 dict형 자료형 2개
    output: 종합 점수 계산이 된 dict 자료형
    """
    user_sum_score_dic = {}
    # 종합 점수 계산 (math*2 + eng)
    for k, math_score in user_math_score_dic.items():
        sum_score = math_score*2
        sum_score += user_eng_score_dic[k]
        user_sum_score_dic[k] = sum_score
    return user_sum_score_dic

def get_user_score_list2(user_math_score_dic, user_eng_score_dic):
    """
    input: 유저의 이름을 key로, 점수를 value로 가지는 dict형 자료형 2개
    output: 종합 점수 계산에 따라 내림차순으로 정렬한 유저의 이름 list
    """
    user_sum_score_dic = calc_user_sum_score(user_math_score_dic, user_eng_score_dic)

    # 종합 점수에 따라 내림차순 정렬
    sorted_user = sorted(user_sum_score_dic.keys(), key=lambda x: user_sum_score_dic[x])
    return sorted_user

print("# Good code")
print(get_user_score_list(user_math_score_dic, user_eng_score_dic))


# LBYL
if os.path.exists(filename):
    with open(filename) as f:
        ...
        

# EAFP
try:
    with open(filename) as f:
        ...
        
except FileNotFoundError as e:
    logger.error(e)
    ...
