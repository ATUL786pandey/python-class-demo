def validate(age):

    if age <= 18:
        raise ValueError ("not eligible for voiting")
    else:
        print("eligible for voiting")

try:
    validate(12)
except ValueError as ve:
    print(ve)

finally:
    print("final block")
