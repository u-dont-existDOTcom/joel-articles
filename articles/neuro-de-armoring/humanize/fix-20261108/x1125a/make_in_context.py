"""The warnings at the top beside his post, for the turn of 2026-11-25: what went into the article (each Human High by
itself) and what is proposed and waits (the three teaching cards, the two short paragraphs still below High), with
every try's link. Paragraph text comes from the article and the post; only labels and notes are typed here.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1125a/make_in_context.py OUT.html
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texts_x1125a as T  # noqa: E402

H = HERE.parents[1]
ROOT = T.ROOT
PG = 'https://www.pangram.com/history/'


def a(u, label):
    return '[%s](%s%s)' % (label, PG, u)


ROWS = [
    {'label': 'P1 · in the article · the label on a line of its own', 'article': '⚠️ CRITICAL MEDICAL DISCLAIMER:',
     'source': [{'quote': '⚠️ CRITICAL MEDICAL DISCLAIMER:', 'from': 'the first paragraph of the section'}],
     'note': 'Your post has this as a bold line above the list of warnings; the import had run it into the DMSO item.'},
    {'label': 'P2 · in the article · DMSO Safety', 'article': 'DMSO Safety: This protocol has you smell DMSO',
     'source': ['⚠️ CRITICAL MEDICAL DISCLAIMER:DMSO Safety'],
     'notes': ['By itself: ' + a('00c16a93-c037-4131-be4a-92e08639fcf8', 'Human Written, one window, High') + ', on try 4.',
               'Earlier tries: ' + a('b6ae4d59-c6af-4d81-8b6c-82eca40299c1', 'try 1, Human with two Medium windows') + '; '
               + a('16b45e52-1788-44e3-970c-b0b823ae7cae', 'try 2, Human with two Medium windows') + '; '
               + a('af48d389-bcad-4fac-bf2f-2e25289edaba', 'try 3, Human, one window, High') + '.',
               'Added by me, for you to approve: what DMSO is and what the protocol uses it for; why glass (it can leach '
               'chemicals out of some plastics); washing lotions and other products off; the smoker\'s caution and the '
               'first sign, feeling weak, both from your own DMSO article.']},
    {'label': 'P3 · in the article · Electrolytes', 'article': 'Electrolytes: This protocol has you eating',
     'source': ['Electrolytes: Consult a doctor'],
     'notes': ['By itself: ' + a('107fdac9-c18d-4518-a639-09950f338556', 'Human Written, one window, High') + ', on try 2 ('
               + a('db02d981-2f00-4ec8-b1d0-7dce7f3e1b18', 'try 1: AI Detected, 40.5%') + ').',
               'Added by me, for you to approve: the reason (the protocol means a lot more potassium, and it can build up '
               'in your blood) and the blood pressure drugs that hold on to potassium (ACE inhibitors and ARBs), both '
               'from your own Electrolytes section.']},
    {'label': 'P4 · in the article · Ethnobotanicals', 'article': 'Ethnobotanicals: The plant medicines in this protocol',
     'source': ['Ethnobotanicals:Iboga and Psilocybin'],
     'notes': ['By itself: ' + a('1b3f5324-df31-4bd8-b823-a19e0a38a012', 'Human Written, one window, High') + ', on try 2 ('
               + a('e9fb1581-dca4-4000-a00d-69f6f4569054', 'try 1: Human Written, one window, High') + ', before "any '
               'medication").',
               'Added by me, for you to approve: what iboga is (an African root bark); that iboga\'s risks are the '
               'serious ones, to the heart and nervous system (from your 5-HTP warning); and "if you take any medication, '
               'check it against my full iboga guide here first". I couldn\'t open the guide from here, so say if it '
               'doesn\'t list medications.']},
    {'label': 'P5 · PROPOSAL, not in the article · teaching card W-ISO', 'text': T.V8['iso'],
     'proposal_of': 'Behavioral Warning (The Isolation Trap):', 'source': ['Behavioral Warning (The Isolation Trap):'],
     'notes': ['Three tries by itself, each one window, AI High: ' + a('2bef0402-3916-4f9c-b1cd-2678afe1b0fd', 'try 1') + ', '
               + a('e4fe5ff4-a18f-4149-9012-602e43efe756', 'try 2') + ', ' + a('11c50d40-e436-4393-be4f-522934cc9c33', 'try 3')
               + '. The article keeps your post\'s paragraph until your version.',
               'Leaves out "because humans are social animals"; adds that holing up alone is the easiest way to cut the '
               'dopamine.']},
    {'label': 'P6 · PROPOSAL, not in the article · The Rule', 'text': T.V4['rule'], 'proposal_of': 'The Rule: Seek',
     'source': ['The Rule: Seek'],
     'notes': ['With the Cognitive Warning after it: ' + a('d733d10c-8ca8-4761-8e03-4ad19be07015', 'Human Written') +
               ': its first sentence Medium, its second High. Not in until every window is High; next turn\'s small steps.',
               'Twice before, beside the Isolation Trap: ' + a('ac07638e-9c45-4297-a281-a4000cf706ba', '100% AI') + ', '
               + a('96a4d41d-ab23-49ca-94c5-5da77d9ce6d3', '100% AI') + ' (the Trap reads 100% AI alone, so those said '
               'nothing about the rule).']},
    {'label': 'P7 · PROPOSAL, not in the article · Cognitive Warning', 'text': T.V9['cog'],
     'proposal_of': 'Cognitive Warning:', 'source': ['Cognitive Warning: As you de-armor'],
     'notes': ['With the paragraph after it: ' + a('d3e4d207-f93b-4ba5-a7c1-d319c4de6074', 'try 1, AI Detected 62.2%') + '; '
               + a('284787bb-3977-4203-a7fe-266746642c33', 'try 2, AI Detected 61.5%') + '; '
               + a('bda984c5-6d7a-4260-9134-7a1ac5800bbb', 'try 3, Human Written, every window Human') + ' (High, Medium, '
               'Low, Medium); ' + a('9ecfeec8-2128-4c18-9d22-11bab918d1cd', 'try 4, Mostly Human Written') + ' (the same '
               'windows). Not in until every window is High.',
               'Added by me: "more ... than you\'re used to" and "which they mostly can\'t" (what the illusion is).']},
    {'label': 'P8 · in the article · Cognitive Warning, second paragraph', 'article': 'Your armored brain also reads',
     'source': ['The armored brain projects'],
     'notes': ['By itself: ' + a('67054583-220a-4f9f-94b8-f421bc4102b9', 'Human Written, one window, High') + ', on try 2 ('
               + a('153b7654-92d0-4721-b482-69479955e095', 'try 1: Human Written, one window, Low') + ').',
               'Your 62a words for the heart rate are kept. Added by me, for you to approve: "at least until", and why '
               'the heart is the test ("since a racing heart means your reasoning brain is offline", with the link to '
               'the Metabolic Red Line). Left out: \'It is calibrated to "Threat," not "Truth."\'']},
    {'label': 'P10 · PROPOSAL, not in the article · teaching card W-AGMINTRO', 'text': T.V8['agm'],
     'proposal_of': 'Agmatine Warning (The Voltage Governor):', 'source': ['Agmatine Warning (The Voltage Governor):'],
     'notes': ['Three tries by itself, each one window, AI High: ' + a('61e59dc5-7acd-488f-be9d-6277cdbdc2d4', 'try 1') + ', '
               + a('08c6a4d2-9228-4ddd-a038-6988c2a72769', 'try 2') + ', ' + a('2829fcb4-fcf2-4f52-b75d-70268695285b', 'try 3')
               + '. The article keeps your post\'s paragraph until your version.',
               'Your Precautions paragraph after it, as it stands: ' + a('afc40e25-fc20-4db8-a220-5c1fb41419d6',
                                                                         'Human Written, one window, High') + '.']},
    {'label': 'P13 · PROPOSAL, not in the article · teaching card W-HTPTOP', 'text': T.V7['htp'],
     'proposal_of': 'Uridine & 5-HTP Warning for Psychedelic Users:',
     'source': ['Uridine & 5-HTP Warning for Psychedelic Users:', 'Rule: do not take 5-HTP on the same day as psychedelics'],
     'notes': ['Three tries by itself: ' + a('de9dc2c7-5af6-4ab3-8070-fbd0eaf7fc0d', 'try 1, 84.9% AI') + '; '
               + a('1b3bfd01-d122-4085-ad46-3824d7028a01', 'try 2 (shown), 67.2% AI') + ', its list Human High and its '
               'rule Human Medium; ' + a('b0b8ebed-8061-4fc0-a1b3-f37c57705130', 'try 3, 100% AI') + '.',
               'In the article now: your post\'s paragraph with its rule sentence ("Rule: do not take 5-HTP on the same '
               'day as a psychedelic trip ...") moved to its end from the head of the uridine paragraph, unchanged, so '
               'everything about 5-HTP is in one place.']},
    {'label': 'P14 · in the article · Uridine', 'article': 'Uridine (the UMP in this protocol)',
     'source': [{'quote': 'Uridine is not serotonergic, but it may still change dream vividness, visual sensitivity, '
                          'craving, and psychedelic tolerance. Do not take UMP on the same day as psychedelics; if '
                          'sensitivity changes, assume your old psychedelic dose may now be too high.',
                 'from': 'the end of the "Rule:" paragraph'}],
     'notes': ['By itself: ' + a('5cdcee71-8073-41fa-a770-6dc2950c0b10', 'Human Written, one window, High') + ', on try 2 ('
               + a('0e296e60-6e5d-4100-8b92-c4d31dc4c760', 'try 1: Human Written, one window, High') + ', before '
               '"starting uridine").',
               'Added by me, for you to approve, each from your own UMP section: the directions (psychedelics can hit '
               'harder, dreams more vivid, cravings weaker), "within a day" (Scott), "take less" on the first trip, '
               'and "I don\'t have studies on it" (your "There\'s no study showing ...").']},
]
MAP = {'title': 'Neuro De-Armoring: the warnings at the top, beside your post',
       'meta': 'Neuro de-armoring · A Complete Guide to Bio-De-Armoring · 2026-11-25',
       'intro': ['Your post on the left, the article or my proposal on the right, with the words I changed marked. Six '
                 'paragraphs are in the article, each Human High by itself. Five are proposals that are not in: three '
                 'wait for your version on the cards page, and two short ones need more small steps from me.',
                 'No compound, dose, unit or timing changes anywhere.'],
       'blocks': [{'headings': ['### A Complete Guide to Bio-De-Armoring'], 'rows': ROWS}]}


def main(out):
    m = HERE / 'IN-CONTEXT-MAP.json'
    m.write_text(json.dumps(MAP, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/render_in_context.py'), str(m), out,
                        '--article', str(H / 'HUMANIZED-SO-FAR.md'), '--source', str(H.parent / 'master.md'),
                        '--against-source', '--source-label', 'Your post'], capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-1500:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
