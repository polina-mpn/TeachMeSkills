def unicorns_to_rainbows(unicorns: list[dict]) -> list[str]:
    return [f"🌈 Rainbow unicorn of color {unicorn['color']}" for unicorn in unicorns]

unicorns = [{"color": "pink"}, {"color": "blue"}, {"color": "sparkly"}]
result = unicorns_to_rainbows(unicorns)
print(result)