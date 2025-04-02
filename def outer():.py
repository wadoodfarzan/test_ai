# def example_function(a, b, *args, c=10, d=20, **kwargs):
#     print(f"a: {a}, b: {b}")
#     print(f"args (extra positional): {args}")
#     print(f"c: {c}, d: {d}")
#     print(f"kwargs (extra keyword): {kwargs}")


# example_function(1, 2, 3, 4, c=30, e=50, f=60)

cellsize = 0.2
src_cellsize = 0.1
factor = round(cellsize * 10) // round(src_cellsize * 10)
print(factor)
