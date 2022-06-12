class Solution:
    def numberToWords(self, num: int) -> str:
        under_twenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                    'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
                    'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                    'Nineteen']

        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
                'Eighty', 'Ninety']

        thousands = ['Thousand', 'Million', 'Billion']

        def to_words(num):
            if num == 0:
                return []

            if num < 20:
                return [under_twenty[num]]

            if num < 100:
                quotient = num // 10
                remainder = num % 10
                return [tens[quotient]] + to_words(remainder)

            if num < 1000:
                quotient = num // 100
                remainder = num % 100
                return [under_twenty[quotient], 'Hundred'] + to_words(remainder)

            for power, thousand in enumerate(thousands, 1):
                if num < 1000 ** (power + 1):
                    quotient = num // 1000 ** power
                    remainder = num % 1000 ** power
                    return to_words(quotient) + [thousand] + to_words(remainder)

        return ' '.join(to_words(num)) or 'Zero'
