class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            if s=="":
                encoded = encoded + ":" + "00"
            else:
                ind_encode = "-".join([str(ord(x)) for x in s])
                encoded = encoded + ":" + ind_encode
        return encoded


    def decode(self, s: str) -> List[str]:
        decode_ls = s.split(":")[1:]
        result = []
        for st in decode_ls:
            if st=="00":
                result.append("")
            else:
                result.append("".join(chr(int(x)) for x in st.split("-")))
        return result

