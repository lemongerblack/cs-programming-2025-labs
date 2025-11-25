def f(x):
    for i in list(x):
        if not str(i).isdigit():
            return tuple(x)
            break
    else:
        return tuple(sorted(list(x)))
print(f(eval(input("введите кортедж пж: "))))