# Regeneration version 3 — fixed 40-passage trial

**Decision:** Both version 3 methods missed their predeclared admission gate. No version 3 regeneration enters training, and no full generation or adapter training was run from these data. Claude subsequently committed a distinct version 4 round-trip trial at `07ba4f137ee29ede64379be4550bdfc985562f5b`; this report is the preserved version 3 evidence.

## Frozen trial and outcomes

The source manifest is `data/human-passages.jsonl` (SHA-256 `56869801ee7f95dfea1681170c745cacf112f93c117a185177c515568c80b089`). Forty training-split regeneration IDs were fixed before either method: 30 version 2 copy failures, H0012/H0062, and eight unprocessed IDs. Both methods used the same fixed set. The Chinese trial kept its first eight final outcomes, then used batch size 32 for the remaining 32. The initial interruption left eight reserved notes calls with no recorded or observed output; they were censored, not counted as attempts. Each was reconciled before reissue. The English-slot fallback used batch size 40.

| Method | Overall | Old 30 | New 8 | Technical 10 | Gate |
|---|---:|---:|---:|---:|---|
| Chinese notes | 24/40 | 22/30 | 1/8 | 7/10 | Fail: overall below 28 |
| English atomic JSON slots | 0/40 | 0/30 | 0/8 | 0/10 | Fail: notes parser rejected all 40, including retries |

The Chinese go gate was at least 28/40 overall, 18/30 old failures, and 5/10 technical. It missed overall by four. The slot fallback retained the same gate. Its 80 model requests comprised an initial and one retry notes request for each passage. No slot notes passed strict JSON/field parsing, so no draft or meaning judgments ran. This observes a formatting failure, not a test of whether slots preserve meaning.

| Genre | Chinese accepted | English slots accepted |
|---|---:|---:|
| email | 1/1 | 0/1 |
| essays_journal | 5/17 | 0/17 |
| letters | 3/4 | 0/4 |
| practical | 8/8 | 0/8 |
| technical | 7/10 | 0/10 |

## Chinese-notes diagnostics

Final rejection reasons can overlap: `ai_claims_in_human` 7, `human_claims_in_ai` 4, `notes_not_substantially_chinese` 4, `no_draft` 4, `draft_truncated` 2, `copy_or_list_guard_failed` 2. The two judge directions are recorded under their exact phase names; a single passage can fail multiple checks.

Among 36 final drafts with a copy-guard measurement, the longest source-word run in notes had median 0.0 and maximum 6. The draft run had median 7.0 and maximum 13. The protected-source share had median 0.15773887865227693 and maximum 0.2992125984251969. These are guard measurements, not Pangram or quality scores.

Chinese trial summary: 40 final outcomes, 24 accepted, 217 saved model requests and 1,682.79 seconds for the batch-32 continuation, in addition to the retained initial eight and model loading. The English-slot fallback ran 816.62 seconds and saved 80 model requests; its peak allocation was 22.75 GiB. The Chinese continuation peaked about 21.98 GiB. Both trials stayed inside Claude’s cumulative time caps. No new Pangram diagnostic was admitted because neither method passed. No version 3 Emulate words were used. Pilot Pangram use remains 48 credits from the earlier 20-draft spot check.

At the signed-in Vast billing check after these trials, replacement instance 53306647 had $5.56 of billed GPU and the original instance $0.11, so the conservative pilot GPU total was $5.67 against the $40 cap. The replacement instance showed $7.92 total charges, including $1.49 storage and $0.87 download, and the account’s displayed credit usage was $8.06. Account-level usage may include unrelated charges. The remaining wallet was $11.94. The instance was then stopped; only storage continued at about $0.11/hour. No worker purchase or additional instance was made.

The complete Chinese request journal, responses, outcome records, immutable interruption snapshot, hashes and receipt are in the private off-instance archive `v3-chinese-complete.tar.gz` (SHA-256 `df7cbef3f7ff2eb594dffa4ded0cebfd150ea25ab682465750a51e593f11d615`). The slot fallback archive is retained on instance 53306647 at `/workspace/reverse-pilot-20260929/trial-v3/slots-complete.tar.gz`; it was not copied off-instance. The instance remains retained. Both methods’ accepted outputs are evidence only, not training admissions.

## Censored calls

All eight had phase `v3_notes_1`, status `CENSORED_NO_OUTPUT` and a hashed pre-recovery snapshot. Log inspection found no output from them. Reservation keys are `(passage, phase, prompt SHA-256)`:

- `H0021` / `v3_notes_1` / `251d25c7d1a7b0f951b6fce8b813d490777eadc7decff0656988d797f71d9c7a`
- `H0023` / `v3_notes_1` / `5622ffd18d6caf8b24fcc4e39523c974fd84ac0d3193b5ee571ae18e9ad1676b`
- `H0026` / `v3_notes_1` / `e62517f9ac0ae9711a80be0690bdd6c86f56b55e5c4c432793046c5212c3bf2f`
- `H0027` / `v3_notes_1` / `37bf6736a7bf9542d13f132fedf09d464404081289aa988fbf09c7597dad2710`
- `H0029` / `v3_notes_1` / `1c876f5edde808f07fba519be7b63d1de157cae264d7a85556d36c5c20f02a99`
- `H0030` / `v3_notes_1` / `29c4855b46f00acbeb30261e2ef645aab76839b9eecd0e7cc83490129ae5655c`
- `H0032` / `v3_notes_1` / `b4b766f6f4a0ed17b67d433dec5a898af71ada82cf492e65e8866b4afd9aa0a8`
- `H0033` / `v3_notes_1` / `99861802d0953dc5053b8c767b936faa34d9ad28e9d508b032a09e30fcf56620`

## Five accepted Chinese triples

These are diagnostic examples selected by the first five accepted passage IDs, without outcome cherry-picking. The English slot method produced none. Each “notes” field below is the exact raw notes response, including FORM and KEEP; the draft is the saved final English text.

### H0002

**Human passage**

```text
Such studies
        can also reveal a lot about the general role of microevolution in species divergence.
        Reinforcement provides a pathway toward the completion of the speciation process.
        Imagine that two divergent populations (potentially even classified as separate species)
        come into contact after a period of allopatry (Figure 1). If the populations have been
        apart for a long time, evolved differences between them will cause a certain degree of
        incompatibility when the populations come together. Often, this incompatibility comes in
        the form of low hybrid fitness (postzygotic isolation) or mismatched mating characteristics
        (premating isolation). The degree of the development of these isolating mechanisms is
        roughly proportional to the genetic distance between the populations, reflecting the fact
        that incompatibilities accumulate over time (Coyne and Orr 1989).
        If the isolating mechanisms between these populations are only partially complete,
        extensive hybridization may occur. This can result in fusion back into a single population,
        or in the swamping of one population's gene pool by the genes of the other (extinction).
```

**Chinese notes response**

```text
FORM:  
Scientific article, third-person perspective  

KEEP:  
- microevolution  
- species divergence  
- Reinforcement  
- speciation process  
- divergent populations  
- separate species  
- allopatry  
- Figure 1  
- low hybrid fitness  
- postzygotic isolation  
- mismatched mating characteristics  
- premating isolation  
- genetic distance  
- incompatibilities accumulate over time  
- Coyne and Orr 1989  
- isolating mechanisms  
- partially complete  
- extensive hybridization  
- fusion back into a single population  
- swamping of one population's gene pool by the genes of the other  
- extinction  

NOTES:  
1. 微进化在物种分化中的普遍作用可以通过此类研究揭示。  
2. 增强作用（Reinforcement）为完成物种形成过程提供了一条路径。  
3. 想象两个分化种群（甚至可能被分类为不同物种）在经历一段异域分布（allopatry）后重新接触（图1）。  
4. 如果这些种群分离时间很长，它们之间演化出的差异会导致一定程度的不相容性。  
5. 这种不相容性通常表现为低杂种适应度（后合子隔离）或配对特征不匹配（交配前隔离）。  
6. 这些隔离机制的发展程度大致与种群之间的遗传距离成正比。  
7. 这反映了不相容性会随着时间积累的事实（Coyne 和 Orr 1989）。  
8. 如果种群之间的隔离机制仅部分完成，可能会发生广泛的杂交。  
9. 这可能导致种群重新融合为单一群体。  
10. 或者导致一个种群的基因库被另一个种群的基因淹没（灭绝）。
```

**English draft**

```text
Scientific article, third-person perspective

The pervasive role of microevolution in species differentiation can be illuminated through such studies. Reinforcement provides a pathway toward the completion of the speciation process. Consider two diverging populations—potentially already classified as distinct species—following a period of allopatric isolation before coming into secondary contact (Figure 1). If the duration of their separation has been sufficiently long, the evolutionary divergence between them may have led to a degree of incompatibility. This incompatibility typically manifests as reduced hybrid fitness (postzygotic isolation) or mismatched mating traits (prezygotic isolation). The extent to which these isolating mechanisms have developed generally correlates positively with the genetic distance between the populations. This pattern reflects the fact that incompatibilities accumulate over time (Coyne and Orr 1989). Should the isolating mechanisms remain only partially established, extensive hybridization may occur, potentially resulting in the reintegration of the populations into a single, undifferentiated gene pool. Alternatively, such hybridization may lead to the genetic swamping of one population by the other, ultimately resulting in the extinction of the less dominant lineage.
```

### H0008

**Human passage**

```text
Densely packed buttresses facing
        seaward create an extraordinary effect of power and beauty, especially
        when they blaze like gold in the setting sun and cast their reflection
        in the pool below. Before entering, have a look at the remarkable
        Portal del Mirador entrance, overlooking Palma’s bay. The 14th-century
        door is a feast of carved stone figurines, including a depiction of the
        Last Supper by Guillem Sagrera. The north door of the cathedral, near
        the 13th-century bell tower, is reserved for those attending religious
        services in the early morning and early evening. Tourists are
        encouraged to visit the cathedral in conjunction with the Cathedral
        Museum next door, a treasure-trove of silver monstrances and
        candelabra, saintly relics, Gothic paintings, and Baroque altars. A
        colossal and ornate early Renaissance doorway in carved stone leads on
        to the oval New Chapter House. From the museum, one enters the
        cathedral.
```

**Chinese notes response**

```text
FORM:  
Narrative description from a third-person tourist guide perspective.

KEEP:  
seaward  
extraordinary effect of power and beauty  
blaze like gold in the setting sun  
cast their reflection in the pool below  
Portal del Mirador entrance  
Palma’s bay  
14th-century door  
feast of carved stone figurines  
depiction of the Last Supper by Guillem Sagrera  
north door of the cathedral  
13th-century bell tower  
religious services in the early morning and early evening  
tourists are encouraged to visit the cathedral in conjunction with the Cathedral Museum next door  
treasure-trove of silver monstrances and candelabra, saintly relics, Gothic paintings, and Baroque altars  
colossal and ornate early Renaissance doorway in carved stone  
oval New Chapter House  
From the museum, one enters the cathedral.

NOTES:  
1. 石砌的支撑墙面向海洋，密集排列，形成一种非凡的力量与美感。  
2. 当这些支撑墙在夕阳中如金子般闪耀，并将倒影投射到下方水池时，这种效果尤为突出。  
3. 进入前，应先观看位于帕尔马湾上方的显著的“展望之门”入口。  
4. 14世纪的门饰满是雕刻的石头人物，其中包括由吉列姆·萨格雷拉创作的“最后的晚餐”图像。  
5. 大教堂的北门靠近13世纪的钟楼，专供清晨和傍晚参加宗教仪式的人使用。  
6. 游客被鼓励将参观大教堂与毗邻的主教座堂博物馆结合进行。  
7. 博物馆内藏有银质圣体匣和烛台、圣徒遗物、哥特式绘画和巴洛克式祭坛，堪称珍宝库。  
8. 一扇巨大而华丽的早期文艺复兴时期石雕门通向椭圆形的新章厅。  
9. 从博物馆进入大教堂。
```

**English draft**

```text
Facing the sea, the stone-reinforced retaining walls rise in dense, deliberate rows, exuding an extraordinary sense of strength and beauty. This effect is most striking at sunset, when the walls glisten like gold and cast their radiant reflections onto the water below. Before entering, visitors should first take in the prominent “Porta del Mirador,” the dramatic gateway situated above the Bay of Palma. Dating from the 14th century, its ornate stonework is richly carved with figures, among them the celebrated depiction of “The Last Supper” by Guillem Sagrera. The cathedral’s northern portal, adjacent to the 13th-century bell tower, was historically reserved for those attending religious services at dawn and dusk. Tourists are encouraged to combine their visit to the cathedral with a tour of the adjacent Cathedral Museum, a treasury of sacred art and relics. Within its halls lie silver reliquaries and candlesticks, saintly relics, Gothic paintings, and Baroque altarpieces—each a masterwork of devotion and craftsmanship. A magnificent and ornate early Renaissance stone door, grand in scale and detail, leads to the elliptical New Chapter Hall. From the museum, the journey into the cathedral begins.
```

### H0009

**Human passage**

```text
556 and no CO2 reductions, we did not find
significant impacts on coal production or electricity prices.
However, in the analysis responding to the Jeffords/Lieberman
request that had NOx, SO2, mercury and CO2 reduction levels similar
to S. 556, we found significant ramifications: approximately a
20-30% decline of coal generation and a 30-50% increase in
electricity prices compared to the reference case (depending on
assumptions of energy technology penetration).
The 90% source-specific control for mercury is also problematic.
We have not seen anything that demonstrates that every coal-fired
power plant would be able to achieve 90% source-specific controls
for mercury by 2007, without considerable fuel switching, which
would be very disruptive to our economy and undermine energy
security. In addition, requiring the same level of reduction at
a
plant that emits 0.1 pounds of mercury and a plant that emits
2000 pounds of mercury - regardless of cost - is neither efficient
nor necessary.
```

**Chinese notes response**

```text
FORM:  
Policy analysis report from a government or regulatory agency, third-person objective perspective.

KEEP:  
556  
CO2 reductions  
significant impacts on coal production or electricity prices  
Jeffords/Lieberman  
NOx, SO2, mercury and CO2 reduction levels  
S. 556  
20-30% decline of coal generation  
30-50% increase in electricity prices  
reference case  
energy technology penetration  
90% source-specific control for mercury  
every coal-fired power plant  
90% source-specific controls for mercury by 2007  
considerable fuel switching  
very disruptive to our economy  
undermine energy security  
a plant that emits 0.1 pounds of mercury  
a plant that emits 2000 pounds of mercury  
same level of reduction  
regardless of cost  
neither efficient nor necessary

NOTES:  
1. 在没有CO2减排的情况下，未发现对煤炭生产和电价有显著影响。  
2. 然而，在回应Jeffords/Lieberman请求的分析中，该分析设定了与S. 556相似的NOx、SO2、汞和CO2减排水平，结果显示有显著后果。  
3. 与参照情景相比，煤炭发电量下降约20-30%。  
4. 与参照情景相比，电价上涨30-50%。  
5. 电价上涨和煤炭发电量下降的程度取决于能源技术渗透的假设。  
6. 90%的汞源特定控制要求存在问题。  
7. 尚未见到任何证据表明，每座燃煤电厂都能在2007年前实现90%的汞源特定控制。  
8. 不进行大量燃料转换，无法实现90%的汞源特定控制。  
9. 大量燃料转换会对经济造成极大破坏。  
10. 大量燃料转换会损害能源安全。  
11. 要求排放0.1磅汞的电厂和排放2000磅汞的电厂实现同等程度的减排，无论成本高低，都是不合理的。  
12. 这种做法既不高效，也不必要。
```

**English draft**

```text
Under a scenario without CO2 emissions reductions, no significant impacts on coal production or electricity prices are observed. However, in an analysis conducted in response to the request by Jeffords and Lieberman, which applied emission reduction levels for NOx, SO2, mercury, and CO2 comparable to those in S. 556, significant consequences emerged. Compared to the reference case, coal-fired electricity generation declined by approximately 20 to 30 percent. Electricity prices increased by 30 to 50 percent relative to the reference scenario. The magnitude of both the decline in coal generation and the rise in electricity prices is sensitive to assumptions regarding the penetration of energy technologies. The requirement for 90 percent mercury-specific control presents substantial challenges, as no evidence has yet been observed to suggest that every coal-fired power plant can achieve such reductions by 2007. Achieving 90 percent mercury control without extensive fuel switching is not feasible. Such large-scale fuel conversion would impose severe economic disruption and undermine energy security. Mandating equivalent levels of emission reductions—regardless of cost—for a plant emitting 0.1 pounds of mercury and one emitting 2,000 pounds of mercury is neither efficient nor justifiable. This approach is fundamentally flawed, as it fails to account for cost disparities and technological feasibility, rendering it both economically imprudent and operationally unreasonable.
```

### H0012

**Human passage**

```text
docno="lists-046-12158926"
name="Neil Soiffer"
email="soiffer@wri.com"
sent="Wed, 5 Jun 1996 19:06:49 -0700"
id="199606060206.AA06946@drizzle.wri.com"
subject="Re: Comments on parsing steps:"
To: dsr@w3.org
Cc: w3c-math-erb@w3.org


     
   
>> Mathematica's parsing, which works in a manner similar to what Bruce
>> describes, has no problem handling complex embellishments.

>I can see value in allowing prefix and postfix operators to act as
>operator embellishments, for instance to add accents to operators or
>to change their relative size, or position.

>If these embellishment prefix and postfix operators have a high
>precedence and hence bind tightly to the adjacent operator then
>I don't see any problems. Am I missing something?

I think that there is a problem with prefix embellishments.
The arguments are technical, so people who don't care can stop reading.
```

**Chinese notes response**

```text
FORM: Email from Neil Soiffer to dsr@w3.org, with Cc to w3c-math-erb@w3.org, discussing parsing steps and operator embellishments.

KEEP:
Mathematica's parsing, which works in a manner similar to what Bruce describes, has no problem handling complex embellishments.
I can see value in allowing prefix and postfix operators to act as operator embellishments, for instance to add accents to operators or to change their relative size, or position.
If these embellishment prefix and postfix operators have a high precedence and hence bind tightly to the adjacent operator then I don't see any problems. Am I missing something?
I think that there is a problem with prefix embellishments.
The arguments are technical, so people who don't care can stop reading.

NOTES:
1. Neil Soiffer 发送了一封电子邮件，收件人为 dsr@w3.org，抄送至 w3c-math-erb@w3.org。
2. 电子邮件的主题为“Re: Comments on parsing steps:”，发送于1996年6月5日19:06:49（UTC-7）。
3. 电子邮件的ID为199606060206.AA06946@drizzle.wri.com。
4. 在回复中提到，Mathematica的解析方式与Bruce所描述的相似，并且能够处理复杂的装饰。
5. 有人认为允许前缀和后缀运算符作为运算符装饰是有价值的，例如用于给运算符添加变音符号，或改变其相对大小或位置。
6. 该人进一步指出，如果这些装饰性的前缀和后缀运算符具有高优先级，从而紧密绑定到相邻的运算符，则看不出有什么问题，并询问是否遗漏了什么。
7. Neil Soiffer认为前缀装饰存在一个问题。
8. 他指出该问题的技术性较强，因此不关心的人可以停止阅读。
```

**English draft**

```text
FORM: Email from Neil Soiffer to dsr@w3.org, with Cc to w3c-math-erb@w3.org, discussing parsing steps and operator embellishments.

On June 5, 1996, at 19:06:49 UTC-7, Neil Soiffer sent an email to dsr@w3.org, with a copy to w3c-math-erb@w3.org, titled “Re: Comments on parsing steps:”, identified by the message ID 199606060206.AA06946@drizzle.wri.com. In the message, he notes that Mathematica’s parsing behavior is similar to what Bruce had described and is capable of handling complex embellishments. He acknowledges that there is value in allowing prefix and postfix operators as operator embellishments, particularly for purposes such as adding diacritical marks or altering the relative size or position of an operator. He further observes that if such embellished operators were assigned high precedence—binding tightly to adjacent operators—there appears to be no obvious issue, and he raises the question of whether anything important might be overlooked. However, Neil Soiffer expresses concern about prefix embellishments, noting that the issue is technically nuanced and therefore advises that those uninterested in the technical details may safely stop reading.
```

### H0014

**Human passage**

```text
Chatterbox Goes Too Far!

            One reason Kathleen Willey's tale of groping and fondling in the Oval Office
seems credible is this: if she were making up a story, she could have made up a
much better one. For example, Willey told Ed Bradley of 60 Minutes that
when Clinton made his pass, she remembers saying to him, "Aren't you afraid
that somebody's going to walk in here?" Not exactly the strongest or most
plaintive objection she might have lodged. The pass itself could easily have
been made cruder, and Willey could have alleged it was repeated--if she'd been
in a fabricating, sympathy-generating mode. Thanks to Time magazine, we
have evidence that when Willey wants to make up a story, she knows how
to pull out all the emotional stops. Time says that in 1995 when Willey
decided to get back at a former lover, Shaun Docking, she told him she was
pregnant.
```

**Chinese notes response**

```text
FORM:  
Testimony from a witness in a political scandal, first-person perspective.

KEEP:  
Kathleen Willey  
groping and fondling  
Oval Office  
Ed Bradley  
60 Minutes  
Clinton  
"Aren't you afraid that somebody's going to walk in here?"  
Time magazine  
1995  
Shaun Docking  
she told him she was pregnant

NOTES:  
1. 凯瑟琳·威尔利（Kathleen Willey）声称在椭圆形办公室内遭到克林顿的性骚扰，包括摸捏行为，这一说法被认为可信。  
2. 如果威尔利在编造故事，她本可以编造一个更可信、更强烈的版本。  
3. 威尔利向爱德·布拉德利（Ed Bradley）在《60分钟》节目中回忆，当克林顿动手时，她记得自己说：“你不怕有人会走进来吗？”  
4. 这句回应并不强烈，也不是最令人同情的抗议。  
5. 克林顿的举动本可以更粗鲁，而威尔利本可以声称这种行为被重复过，如果她当时处于编造故事、博取同情的模式中。  
6. 《时代》杂志提供了证据，显示当威尔利想编造故事时，她知道如何调动所有情感元素。  
7. 1995年，威尔利决定报复前男友肖恩·多金（Shaun Docking），于是告诉他她怀孕了。
```

**English draft**

```text
FORM: Testimony from a witness in a political scandal, first-person perspective.

Kathleen Willey stated that she was sexually harassed by Clinton in the Oval Office, including acts of touching and groping, and her account is considered credible. If she had been fabricating the story, she could have invented a more believable and emotionally charged version. She recalled, in an interview with Ed Bradley on 60 Minutes, saying to Clinton as he touched her: “You’re not afraid someone might walk in?” That response was not forceful, nor was it the most sympathetic protest one might expect from a victim. Clinton’s actions could have been more overtly aggressive, and Willey could have claimed the incident occurred multiple times if she were constructing a narrative to elicit sympathy. Yet, The Time magazine provided evidence that when Willey chose to fabricate a story, she knew how to summon every emotional element. In 1995, she decided to retaliate against her former boyfriend, Shaun Docking, by telling him she was pregnant.
```
