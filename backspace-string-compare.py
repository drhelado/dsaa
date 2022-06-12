class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        sp, tp = len(s) - 1, len(t) - 1

        ss, ts = 0, 0

        # loop both strings backwards
        while sp >=0 or tp >= 0:

            while sp >= 0:
                if s[sp] == '#':
                    ss += 1
                    sp -= 1
                elif ss > 0:
                    ss -= 1
                    sp -= 1
                else:
                    break

            while tp >= 0:
                if t[tp] == '#':
                    ts += 1
                    tp -= 1
                elif ts > 0:
                    ts -= 1
                    tp -= 1
                else:
                    break

            if sp >= 0 and tp >= 0 and s[sp] != t[tp]:
                return False

            s_finished = (sp >= 0)
            t_finished = (tp >= 0)
            if s_finished and not t_finished or not s_finished and t_finished:
                return False

            sp -= 1
            tp -= 1

        return True
