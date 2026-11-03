import random
from selection_sort import selection_sort
from insertion_sort import insertion_sort

def inversions(a):
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a))
               if a[i] > a[j])

def random_tests(trials=2000, seed=1):
    rnd = random.Random(seed)
    for _ in range(trials):
        n = rnd.randint(1, 25)
        data = [rnd.randint(1, 50) for _ in range(n)]
        expected = sorted(data)
        s, sc, _ = selection_sort(data.copy())
        t, _, ia = insertion_sort(data.copy())
        assert s == expected and t == expected
        assert sc == n * (n - 1) // 2 + (n - 1)
        assert ia == 3 * (n - 1) + 2 * inversions(data)
    return trials

def stability_demo():
    data = [(2, "a"), (2, "b"), (1, "c")]
    key = lambda t: t[0]
    s = selection_sort(data.copy(), key=key)[0]
    t = insertion_sort(data.copy(), key=key)[0]
    return s, t

def measure(n, trials=50, seed=7):
    rnd = random.Random(seed + n)
    sc = sa = ic = ia = 0
    for _ in range(trials):
        data = [rnd.randint(1, 10**6) for _ in range(n)]
        _, c1, a1 = selection_sort(data.copy()); sc += c1; sa += a1
        _, c2, a2 = insertion_sort(data.copy()); ic += c2; ia += a2
    rev = list(range(n, 0, -1))
    _, _, rev_sel_a = selection_sort(rev.copy())
    _, rev_ins_c, _ = insertion_sort(rev.copy())
    return dict(n=n, sel_c=sc / trials, sel_a=sa / trials,
                ins_c=ic / trials, ins_a=ia / trials,
                rev_sel_a=rev_sel_a, rev_ins_c=rev_ins_c)

if __name__ == "__main__":
    print("Пройшло випадкових перевірок:", random_tests())
    print("Стійкість, вхід [(2,a),(2,b),(1,c)]:")
    print("  вибір:", stability_demo()[0])
    print("  вставки:", stability_demo()[1])
    print("Замір (середнє за 50 масивів; найгірший вхід - спадний):")
    for n in (10, 50, 100, 200, 400):
        print(measure(n))
