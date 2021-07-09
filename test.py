
import base64

sample_string = "1234"
# sample_string_bytes = sample_string.encode("ascii")

print(base64.b64encode(sample_string.encode("ascii")).decode("ascii"))
# base64_string = base64_bytes

# print(f"Encoded string: {base64_string}")
