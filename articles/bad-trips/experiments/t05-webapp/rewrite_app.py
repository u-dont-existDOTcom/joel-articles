#!/usr/bin/env python3
"""rewrite_app.py - the Bad Trip Triage web app, rewritten to match the guide (Joel, 2026-11-04 11:35 UTC: "rewrite web
app to match the guide if you can, but if you're blockewd by guardrails then keep checlist int he guide yeah").

Reads the app as it is live (the Elementor HTML widget of https://ibogaqueen.com/1625-2/: its style, its #btg-app markup
and its script, cut from the page's source by cut_widget.py) and writes the widget rewritten: every change below is an
exact replacement that must match the stated number of times, or the script stops. What changes, and why, is the
turn-4 check (../t04-webapp/WEB-APP-CHECK.md):

1. Medical danger: the app said not to try a home rescue; the guide's step 1 says get help and rescue in parallel.
2. Amounts: the app gave none ("does not invent a universal dose"); the guide's own are put back in its words: humic acid
   (smell first, then a 5mg lick), how DMSO is drunk (diluted, sipped), magnesium chloride (about a gram a minute for
   around twenty minutes, in his experience, with his kidney caution), beach morning glory (a whole leaf can end a trip).
3. Remedies the app left out: humic acid and the Metta NMT sniffer in the brain-damage branch, niacin as the backup trip
   killer, coffee cherry for nausea, sending an entity love, Buteyko-style breathing by name.
4. The gut answer leads with his first thought, zeolite and the ZHoly3O ferment, as the guide's step 10 does; its
   charcoal line is the guide's instead of "Do not use activated charcoal at home unless ...".
5. The field notes inside each answer open by default and carry the guide's own label ("Personal field signal") instead
   of "Personal observation - not validated treatment"; the table's "Evidence-weighted caution" column becomes what the
   guide itself says to watch for, row by row (the two rue rows, which the guide doesn't have, keep the app's text).

  python3 rewrite_app.py IN.html OUT.html
"""
import hashlib
import sys

R = [
    # 1. medical danger: help and field rescue in parallel (the guide's step 1, word for word where it can be)
    ('<strong>Do not treat this as shadow work or try a home rescue protocol.</strong> Call emergency services now.',
     '<strong>Call emergency services now, and give basic first aid and any appropriate immediate rescue measures while '
     'help comes.</strong> Medical help and field rescue can happen in parallel. Please don’t spiritually process a body '
     'that is going under.', 1),
    # 2. DMSO, with humic acid and the sniffer (the guide's Core Order, step 1), and how it is drunk (its side effects)
    ('Use DMSO now under the guide’s field plan while emergency evaluation is activated.',
     'Use DMSO now while emergency evaluation is activated, and smell humic acid; if that doesn’t help, take a 5mg lick '
     'of it.', 1),
    ('<strong>Use DMSO now under the guide’s field plan.</strong>',
     '<strong>Use DMSO now. Smell humic acid first; if that doesn’t help, take a 5mg lick of it. Smell the Metta NMT '
     'sniffer.</strong> When drinking DMSO, dilute it in water, juice, or milk and sip gradually.', 1),
    ('Use DMSO now under the guide’s field plan while checking wakefulness,',
     'Use DMSO now, and smell humic acid (if that doesn’t help, take a 5mg lick of it), while checking wakefulness,', 1),
    ('DMSO under the guide’s field plan', 'DMSO right away', 5),
    ('The exception is the guide’s DMSO-first field plan when acute neurological injury is suspected. For a psychedelic '
     'brain-damage concern, prepare to terminate the trip with the person’s familiar <em>Ipomoea pes-caprae</em> plan once '
     'swallowing and basic stability are established;',
     'The exception is DMSO first when acute neurological injury is suspected. For a psychedelic brain-damage concern, '
     'prepare to stop the trip with beach morning glory (<em>Ipomoea pes-caprae</em>) once swallowing and basic stability '
     'are established (in the author’s experience a whole leaf can easily end a trip);', 1),
    # beach morning glory, as the guide says it
    ('terminate the trip with the familiar <em>Ipomoea pes-caprae</em> plan.',
     'stop the trip with beach morning glory (<em>Ipomoea pes-caprae</em>).', 1),
    ('then the person’s familiar pes-caprae trip-abort plan.',
     'then beach morning glory (pes-caprae) to stop the trip: in the author’s experience a whole leaf can easily end it.', 1),
    ('After DMSO, use the person’s familiar <em>Ipomoea pes-caprae</em> trip-abort plan.',
     'After DMSO, use beach morning glory (<em>Ipomoea pes-caprae</em>) to stop the trip cold and fast: in the author’s '
     'experience a whole leaf can easily end it.', 1),
    ("'If preparation or amount is not already known from the written guide or an existing rescue plan, do not improvise it here.',",
     "'Without beach morning glory, flushing niacin is the guide’s backup trip killer (not sustained-release niacin or the "
     "no-flush form).',", 1),
    ('<strong>Trip termination is the goal:</strong> use the person’s familiar <em>Ipomoea pes-caprae</em> trip-abort plan.',
     '<strong>Trip termination is the goal:</strong> use beach morning glory (<em>Ipomoea pes-caprae</em>): in the '
     'author’s experience a whole leaf can easily end the trip.', 1),
    ('Use the familiar <em>Ipomoea pes-caprae</em> trip-abort plan rather than stacking random calming remedies.',
     'Use beach morning glory (<em>Ipomoea pes-caprae</em>), the guide’s sledgehammer for stopping a trip cold and fast, '
     'rather than stacking random calming remedies. In the author’s experience a whole leaf can easily end the trip and '
     'may prevent tripping for days afterward. Without it, flushing niacin is the backup trip killer (not sustained-release '
     'niacin or the no-flush form).', 1),
    ("'If preparation or amount is not already known from the full guide or an existing rescue plan, do not invent it in this app.',",
     '', 1),
    ('use the familiar Ipomoea pes-caprae trip-abort plan after DMSO.',
     'use beach morning glory (Ipomoea pes-caprae) after DMSO; a whole leaf can easily end the trip.', 1),
    # magnesium chloride, in his words, with his kidney caution
    ('use the familiar magnesium-chloride plan while reassessing whether the jaw releases.</p><ul><li>The author’s repeated '
     'experience used Dead Sea magnesium chloride hexahydrate flakes dissolved in water. Exact quantities and personal '
     'tolerance belong in the full guide, not an improvised app dose.</li>',
     'take magnesium chloride until the jaw fully releases.</p><ul><li>The author has dissolved Dead Sea magnesium chloride '
     'hexahydrate flakes in water and taken approximately one gram per minute orally for around twenty minutes before his '
     'jaw fully released. He has tolerated around twenty grams without diarrhea; for him, diarrhea appeared only above '
     'roughly forty grams. A token dose may not be enough.</li>', 1),
    ('<li>Kidney impairment raises magnesium-clearance concern, but MDMA itself is the larger adjacent danger.</li>',
     '<li>People with impaired kidneys need to be more cautious with large, rapid magnesium doses, because they may not '
     'clear magnesium normally, but they should be far more worried about the MDMA: treat the situation as higher-risk and '
     'get help sooner.</li>', 1),
    ('use the familiar magnesium-chloride plan and reassess whether jaw and muscle tension release.',
     'take magnesium chloride (the author dissolves Dead Sea magnesium chloride hexahydrate flakes in water and takes '
     'approximately one gram per minute for around twenty minutes) and reassess whether jaw and muscle tension release.', 1),
    ("'If fully conscious and able to swallow, use the familiar magnesium-chloride plan and reassess whether the jaw fully "
     "releases; one token dose may not answer the question.',",
     "'If fully conscious and able to swallow, take magnesium chloride until the jaw fully releases: the author dissolves "
     "Dead Sea magnesium chloride hexahydrate flakes in water and takes approximately one gram per minute for around "
     "twenty minutes. A token dose may not be enough.',", 1),
    ('<p class="btg-small">The author’s detailed repeated oral magnesium-chloride-hexahydrate experience remains in the full '
     'guide. This app does not invent a universal dose.</p>',
     '<p class="btg-small">People with impaired kidneys need to be more cautious with large, rapid magnesium doses, because '
     'they may not clear magnesium normally, but they should be far more worried about the MDMA: treat the situation as '
     'higher-risk and get help sooner.</p>', 1),
    ('use the familiar magnesium-chloride plan only if fully conscious and able to swallow, and reassess jaw release.',
     'take magnesium chloride (about a gram a minute for around twenty minutes, in the author’s experience) only if fully '
     'conscious and able to swallow, and reassess jaw release.', 1),
    # 4. the gut: his first thought leads, and the guide's charcoal line
    ('<p>Treat nausea, diarrhea, and a “dirty/toxic” body feeling as symptoms—not proof of a specific detox mechanism.</p>',
     '<p>Nausea, diarrhea, a dirty or toxic feeling, or a parasite-die-off feeling may need body-level support. The '
     'author’s first thought here is ozonated zeolite (or the ZHoly3O ferment, smelled first) rather than charcoal, because '
     'charcoal can reduce the trip and bind many substances.</p>', 1),
    ("'Do not use activated charcoal at home unless Poison Control or a clinician specifically directs it.'",
     "'Activated charcoal can help gut toxicity, but it adsorbs drugs, including medicines somebody depends on, and it can "
     "flatten the trip. Tell the medics if charcoal was taken.'", 1),
    # 3. nausea: coffee cherry, and the guide's pes-caprae line
    ('<strong>Want to preserve the trip?</strong> Use non-aborting nausea and setting support first. Pes-caprae may stop the '
     'trip because the difference between nausea relief and trip abortion is narrow in the author’s experience.',
     '<strong>Want to preserve the trip?</strong> Eating a couple of coffee cherries helps the author’s nausea, though it '
     'may also extend the trip. A tiny nibble of beach morning glory can sometimes smooth nausea, but the difference between '
     'that and a trip-ending amount is narrow.', 1),
    # entities: sending love (the guide's Demons, Jinn, Entities)
    ("'Invite loving awareness only after the person is stable enough to reach it.',",
     "'The author found that fighting demons and jinn didn’t help, and sending love did. When an entity seemed to attack him "
     "and another person, it left within seconds once he sent it love (“Love Thy Enemy”).',", 1),
    # breathing: Buteyko-style, as the guide's grounding menu says it
    ('gentle reduced nasal breathing may help; never strain or use long breath-holds while intoxicated.',
     'gentle Buteyko-style reduced breathing may help: breathe softly and slowly through the nose, taking in slightly less '
     'air than you want until there is faint air hunger. Never strain or use long breath-holds while intoxicated.', 2),
    ('longer exhale or gentle reduced nasal breathing,', 'longer exhale or gentle Buteyko-style reduced breathing,', 1),
    # 5. the field notes: open, with the guide's own label
    ('<details><summary>How the updated guide’s personal field notes relate</summary>',
     '<details open><summary>The guide’s field notes</summary>', 1),
    ('<span class="btg-badge btg-badge--personal">Personal observation—not validated treatment</span>',
     '<span class="btg-badge btg-badge--personal">Personal field signal</span>', 1),
    ('<p class="btg-small">These observations supplement the live routing. DMSO, psychedelic pes-caprae trip termination, and '
     'the MDMA magnesium branch appear only where the current pattern matches. Do not use them to delay care or invent '
     'dosing.</p>',
     '<p class="btg-small">A personal field signal is what the author has repeatedly observed in himself or other people '
     '(the guide’s own label). When there are danger signs, use these alongside medical help, not instead of it.</p>', 1),
    # the table: what the guide itself says to watch for
    ('Evidence-weighted caution', 'What the guide says to watch for', 1),
    ('No established evidence for acute psychedelic distress; product quality, contamination, histamine reactions, '
     'medication/substance binding, and aspiration risk can change the situation. A “toxic feeling” is not a diagnosis.',
     'A spoonful of ferment may cause itching in somebody low in histamine-processing bacteria, which then needs activated '
     'charcoal to reduce gut histamine. Zeolite has to be prepared correctly: many products did nothing for the author.', 1),
    ('This is a personal preparation note, not validated treatment. Do not inhale ozone gas; ozone is a respiratory hazard. '
     'Do not use by mouth if vomiting, confused, drowsy, or medically unstable.',
     'Ozonate the water, never inhale ozone gas. Use glass, since ozone destroys plastic, and keep the zeolite away from '
     'metal.', 1),
    ('Used clinically only for selected poisonings. It can bind medicines/substances and creates aspiration risk; use only '
     'when appropriate and never with vomiting, impaired consciousness, seizure risk, or unprotected airway.',
     'It adsorbs drugs, including medicines somebody depends on, and can flatten the trip. Use it cautiously around '
     'necessary medicines, and tell the medics if charcoal was taken.', 1),
    ('Field evidence rather than a validated clinical antidote. Plant identity matters. Do not generalize the route to MDMA; '
     'no preparation or dose is invented here.',
     'A tiny nibble can smooth nausea, but the difference between that and a trip-ending amount is narrow; a whole leaf can '
     'easily end the trip and may prevent tripping for days. Even the broken, juicy part of a leaf on sensitive skin can '
     'affect the author. Related plants did not work the same way, and there are no data yet that it aborts MDMA.', 1),
    ('No established clinical evidence for this purpose. Ozone gas should not be inhaled; charcoal can bind '
     'medicines/substances and has aspiration risk when vomiting, drowsy, seizing, or airway safety is unclear. Not an '
     'emergency treatment.',
     'Don’t inhale ozone: the water is used after ozonation has ended and the residual ozone has dissipated.', 1),
    ('Do not treat as medical care. Avoid drinking shungite water unless properly washed and quality-checked; published '
     'drinking-water research reports metal leaching from shungite, including lead, cadmium, nickel, and arsenic.',
     'Shungite should not be drunk unless it has been properly washed of heavy metals.', 1),
    ('Repeated personal experience plus preclinical and limited human signals do not establish complete acute stroke '
     'treatment. Use it in parallel with urgent evaluation when focal signs or unknown stability are present.',
     'Use it while someone calls medics when there are objective stroke-like signs. Don’t put it on dirty skin, and dilute '
     'it when drinking. It may worsen a cluster headache and may release histamine (caution with MCAS). If someone is '
     'worried about a bleed, the author would probably skip it, depending on how severe the issue is.', 1),
    ('Do not invent a dose in the app. Use only when fully conscious and able to swallow. Kidney impairment raises '
     'accumulation risk, while serious MDMA toxicity may involve several electrolytes, heat, serotonin toxicity, '
     'rhabdomyolysis, or rhythm disturbance.',
     'Only when fully conscious and able to swallow. The author takes approximately one gram per minute for around twenty '
     'minutes. People with impaired kidneys need more caution with large, rapid doses, but the MDMA is the bigger worry: '
     'get help sooner.', 1),
    ('Not a validated psychedelic antidote; flushing, GI effects, glucose changes, liver risk, and medication interactions '
     'can occur—especially with higher or repeated doses.',
     'The flush (an itchy, sunburn-like heat), heartburn, and drowsiness with poor sleep. Higher or repeated doses carry real '
     'risk, especially with liver problems, alcohol, or medications. Avoid sustained-release and no-flush niacin.', 1),
    ('External grounding may be benign; do not drink seawater, and never substitute it for medical care.',
     'Direct contact with the water matters: touching the outside of a bottle doesn’t do it.', 1),
    # the hedges left once the amounts are in
    ('Use the live branch, not a random stack. DMSO does not replace imaging or emergency treatment; pes-caprae is not '
     'generalized to MDMA; magnesium and other oral measures require full consciousness and safe swallowing. Do not '
     'improvise a preparation or dose that is not already known from the guide or an existing rescue plan.',
     'Use the live branch, not a random stack. DMSO goes alongside imaging and emergency treatment; there are no data yet '
     'that pes-caprae aborts MDMA; magnesium and other oral measures need full consciousness and safe swallowing.', 1),
    ('If cyproheptadine is already part of a familiar rescue plan and the person is fully alert and can swallow, it may be '
     'used in parallel; evidence for improved major outcomes remains uncertain. Do not improvise charcoal or other remedies '
     'in an impaired airway, active seizure, uncontrolled vomiting, or caustic-ingestion situation.',
     'If the person is fully alert and able to swallow, the guide gives cyproheptadine early, alongside the cooling and the '
     'help: case reports describe rapid improvement, while a recent systematic review found the evidence for major outcomes '
     'inconclusive. Nothing by mouth with an impaired airway, an active seizure, uncontrolled vomiting, or a caustic '
     'ingestion.', 1),
    ("'Use only the exact familiar rescue-plan steps already chosen while sober. Do not invent or optimize a dose inside this app.'",
     "'Follow the rescue plan chosen while sober.'", 1),
    # the app's version
    ('data-version="2026-07-19-v7"', 'data-version="2026-11-04-v8"', 1),
]


def main(src, dst):
    s = open(src, encoding='utf-8').read()
    before = hashlib.sha256(s.encode()).hexdigest()
    for old, new, n in R:
        got = s.count(old)
        if got != n:
            raise SystemExit('expected %d of %r, found %d' % (n, old[:90], got))
        s = s.replace(old, new)
    open(dst, 'w', encoding='utf-8').write(s)
    print('%d changes; %s (%s) -> %s (%s)' % (len(R), src, before[:12], dst, hashlib.sha256(s.encode()).hexdigest()[:12]))


if __name__ == '__main__':
    main(*sys.argv[1:3])
