def acmTeam(topic):
    max_topics = 0
    n = 0
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            temp = 0
            for k in range(len(topic[i])):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    temp += 1
            if temp == max_topics:
                n += 1
            elif temp > max_topics:
                max_topics = temp
                n = 1
    return max_topics, n


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
