from learntools.core import *
from learntools.core.problem import injected

correct_buyer_list = ["Alice", "Bob", "Li Hua", "hypoxanthine", "Asta"]

class CrazyThursday(FunctionProblem):
    _var = 'calculate_price'
    _test_cases = [
        ((0, 0, 0), 0),
        ((1, 1, 1), 14),            
        ((2, 1, 3), 28),
        ((8, 5, 6), 102),
        ((10, 10, 0), 120),
        ((99, 100, 101), 1395),
    ]
    _hint = (
        "一份鸡块加一份薯条的套餐比单买更便宜，所以你应该尽可能选择买套餐\n\n"
        "计算出你最多买多少份套餐，这样子才最省钱\n\n"
        "剩下的需要单买\n\n"
    )
    
    _solution = CS(
        """
        def calculate_price(nuggs, fries, drink):
            combo = min(nuggs, fries)
            nuggs -= combo
            fries -= combo
            return combo * 12 + nuggs * 10 + fries * 5 + drink * 2
        """
    )
    
class VMe50(CodingProblem):
    _var = 'buyer_list'
    _hint = (
        "使用 list 的方法(method)\n\n"
        "`append` 方法可以添加元素到列表的末尾\n\n"
        "`remove` 方法可以删除列表中的元素\n\n"
    )
    _solution = (
        "`buyer_list.remove('Zambar')`\n\n"
        "`buyer_list.append('Asta')`\n\n"
        "你也许使用了 `buyer_list[3] = 'Asta'`，然后得到了正确结果\n\n"
        "但是试想，对于一个很长的，在代码运行的时候才能确定每个元素是什么的列表，你怎么知道第几个元素是 'Zambar'，第几个个元素是 'Asta'？\n\n"
        "以及，并不是每次都需要删除恰好一个并且再添加一个\n\n"
    )
    
    def check(self, buyer_list):
        
        for buyer in buyer_list:
            assert isinstance(buyer, str), "你的列表里面有不是字符串的元素"
        
        assert isinstance(buyer_list, list), "你直接修改了 buyer_list，这是不对的"
        assert set(buyer_list) - set(correct_buyer_list) == set(), f"你的列表里面多出来了 {set(buyer_list) - set(correct_buyer_list)}"
        
        for buyer in correct_buyer_list:
            assert buyer in buyer_list, f"你的列表里面缺少 {buyer}"
            assert buyer_list.count(buyer) == 1, f"你的列表里面有重复的 {buyer}"


class CalculateGrade(FunctionProblem):
    _var = 'calculate_grade'
    _test_cases = [
        ([(89, 0.3), (95, 0.2), (90, 0.5)], 'A'),
        ([(95, 0.038958269955346445), (91, 0.1274809529891583), (100, 0.20688666688159418), (73, 0.1377235567405559), (96, 0.258927772723771), (98, 0.23002278070957421)], 'A'),
        ([(77, 0.08304329284042876), (86, 0.2572730260338583), (70, 0.020586177995970737), (24, 0.005913013630216862), (93, 0.3140997464209337), (97, 0.3190847430785916)], 'A'),
        ([(98, 0.2245638636480294), (96, 0.6558890536986353), (20, 0.03639503632398924), (3, 0.030049536891747903), (92, 0.053102509437598214)], 'A'),
        ([(42, 0.09134680210078487), (84, 0.39378668871150163), (91, 0.14773615110119342), (56, 0.04282926641051223), (93, 0.3243010916760078)], 'B'),
        ([(79, 0.3779103847581755), (54, 0.045691045010851895), (73, 0.17566288045649514), (49, 0.04084387519281836), (96, 0.35989181458165914)], 'B'),
        ([(73, 0.08199847728124954), (91, 0.07572775457450748), (42, 0.099246245996973), (99, 0.2241130703813835), (84, 0.059251169859224635), (99, 0.4596632819066618)], 'B'),
        ([(74, 0.2589231818126907), (83, 0.1184821607028616), (15, 0.05568638866140789), (81, 0.2349199801037073), (50, 0.17289254462634523), (96, 0.1590957440929873)], 'C'),
        ([(86, 0.25759777570311937), (54, 0.017662002312063073), (45, 0.1718394814718099), (76, 0.3129929387876992), (50, 0.0056492335214150405), (41, 0.004564361431982172), (95, 0.10780893099056946), (72, 0.12188527578134176)], 'C'),
        ([(91, 0.11938906946626239), (76, 0.13415320026923017), (41, 0.2493460860568045), (87, 0.14379968779577879), (86, 0.3533119564119242)], 'C'),
        ([(19, 0.14228718289309092), (80, 0.09627293500818875), (42, 0.1869926864176728), (84, 0.18307889065369845), (69, 0.18904624315103072), (93, 0.11162187876087246), (85, 0.06537787761635594), (86, 0.025322305499090043)], 'D'),
        ([(90, 0.1658987796538013), (93, 0.11128097598218514), (70, 0.01643577800259932), (11, 0.14778135374274623), (56, 0.18732959065403107), (92, 0.17911661516462007), (75, 0.1921569068000169)], 'D'),
        ([(95, 0.17149395599698652), (82, 0.0687864698369924), (91, 0.13533369411343418), (59, 0.052716715014989375), (43, 0.1389702582526674), (37, 0.24684989435819787), (6, 0.0682572657710476), (68, 0.11759174665568463)], 'D'),
        ([(22, 0.1655540988614477), (27, 0.24143474070933243), (67, 0.2128635069561679), (21, 0.2162461888409565), (83, 0.16390146463209548)], 'F'),
        ([(3, 0.2947417486638051), (23, 0.06561996157850017), (68, 0.18228155045566083), (34, 0.20277383625647236), (25, 0.25458290304556147)], 'F'),
        ([(51, 0.002811960924540746), (30, 0.17614242266393546), (34, 0.16418867327416242), (63, 0.14688003827992788), (20, 0.3176603911403914), (3, 0.04258646142479604), (67, 0.14973005229224598)], 'F')
    ]
    _hint = (
        "根据类型标注，我们可以知道 s_p_list 是一个列表，列表里面的每个元素是里面有两个元素的元组，第一个是代表分数的整数，第二个是代表这个分数的权重的浮点数\n\n"
        "我们可以通过 for 循环和 unpacking 来更简便地遍历这个列表\n\n"
        "最后的一连串 if 语句是为了根据总分数来判断最后的等级，但是你可以手动模拟一下\n\n"
        "假如 `total_score` 是 95，在运行完第一个 `if` 的代码块之后，又会运行哪部分代码？\n\n"
    )
    _solution = CS(
        """
        def calculate_grade(s_p_list: List[Tuple[int, float]]) -> str:
            total_score = 0
            # 用 unpacking 把元组的两个元素分别赋值给 score 和 percentage
            for score, percentage in s_p_list:
                total_score += score * percentage
            result = "No grade"
            if total_score >= 90:
                result = "A"
            elif total_score >= 80: # 使用 elif 可以避免重复判断
                result = "B"
            elif total_score >= 70:
                result = "C"
            elif total_score >= 60:
                result = "D"
            elif total_score < 60:
                result = "F"
            return result
        """
    )

qvars = bind_exercises(globals(), [
    CrazyThursday,
    VMe50,
    CalculateGrade
],
    start=1,
)
__all__ = list(qvars)
