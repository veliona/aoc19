with open(f"data.txt") as f:
    content = f.readlines()
    numbers = [x.strip() for x in content][0].split(",")
    numbers = [int(x) for x in numbers]