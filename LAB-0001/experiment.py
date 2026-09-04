"""LAB-0001: 用可见的状态转换演示 1 + 1。"""


def show(value):
    return value or "(empty)"


def run_rule(left, right, rule_name):
    step = 0
    print(f"step {step}: {show(left)} + {show(right)}")

    while right:
        if rule_name == "move":
            left = left + "|"   # 把右边的一根棒移到左边
        elif rule_name == "discard":
            pass                # 取出后不放到左边

        right = right[:-1]      # 从右边取出一根棒
        step += 1
        print(f"step {step}: {show(left)} + {show(right)}")

    return len(left)


first = "|"
second = "|"

print(f"Input: {first} + {second}\n")

print("[correct rule: move]")
correct_result = run_rule(first, second, "move")
print(f"decoded result: {correct_result}\n")

print("[counterfactual rule: discard]")
wrong_result = run_rule(first, second, "discard")
print(f"decoded result: {wrong_result}")
