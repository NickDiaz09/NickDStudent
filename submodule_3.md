---
layout: post
title: "Truth Scanner"
description: "Third line of defense from foregin invaders"
permalink: /digital-famine/media-lit/submodule_3/
parent: "Analytics/Admin"
team: "Scratchers"
submodule: 3
categories: [CSP, Submodule, Analytics/Admin]
tags: [analytics, submodule, curators]
breadcrumb: true
author: "Adhav, Ethan, Rishabh"
date: 2025-10-28
---

# Truth Scanner

# Interactive JavaScript/Python Quiz (HTML + JS)

```html
<div id="quiz">
  <div style="margin-bottom:10px;color: white;font-weight:bold;">
    <label><input type="radio" name="lang" value="js" checked> JavaScript</label>
    <label style="margin-left:10px;color: white;font-weight:bold;"><input type="radio" name="lang" value="py"> Python</label>
  </div>

  <div id="card" style="border:1px solid #ccc;padding:12px;border-radius:6px;background: #bc7e7eff;">
    <h3 id="qnum">Question 1</h3>
    <pre id="code" style="background:#272822;color: #f8f8f2;padding:10px;border-radius:4px;overflow:auto;"></pre>
    <div id="choices"></div>
    <div style="margin-top:8px;">
      <button id="submit">Submit</button>
      <button id="next" style="margin-left:8px;">Next</button>
      <button id="explain" style="margin-left:8px;">Show Explanation</button>
    </div>
    <p id="result" style="font-weight:bold;margin-top:8px;color:black"></p>
    <div id="explainText" style="margin-top:6px;color:#333;"></div>
  </div>
</div>

<style>
  button {
    background-color: #5e3434ff;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 14px;
    font-family: "Segoe UI", sans-serif;
    cursor: pointer;
    transition: background-color 0.2s ease, transform 0.1s ease;
    margin-left: 8px;
  }

  button:first-child {
    margin-left: 0;
  }

  button:hover {
    background-color: #5e3434ff;
    transform: translateY(-2px);
  }

  button:active {
    transform: translateY(0);
  }
</style>

<script>
(function(){
  const questions = [
    {
      codeJS: "for (let i = 0; i < 3; i++) {\n  console.log(i);\n}",
      codePy: "for i in range(3):\n    print(i)",
      choices: ["0 1 2", "1 2 3", "0 1 2 3", "Error"],
      answer: 0,
      explain: "Loops start at 0 and run while i < 3, producing 0,1,2."
    },
    {
      codeJS: "let i = 0;\nwhile (i < 3) {\n  i += 2;\n  console.log(i);\n}",
      codePy: "i = 0\nwhile i < 3:\n    i += 2\n    print(i)",
      choices: ["0 2", "2 4", "2", "0 1 2"],
      answer: 1,
      explain: "Each loop iteration increases i by 2 then prints. Values printed: 2 then 4."
    },
    {
      codeJS: "const arr = [1,2,3];\nfor (const x of arr) console.log(x * 2);",
      codePy: "for x in [1,2,3]:\n    print(x * 2)",
      choices: ["2 4 6", "1 2 3", "2,4,6,8", "Error"],
      answer: 0,
      explain: "Each element is multiplied by 2: 2,4,6."
    },
    ...
    {
      codeJS: "const arr = [1,2,3,4];\nlet sum=0;\nfor(const x of arr){\n  if(x%2===0) continue;\n  sum+=x;\n}\nconsole.log(sum);",
      codePy: "arr = [1,2,3,4]\nsum = 0\nfor x in arr:\n    if x % 2 == 0:\n        continue\n    sum += x\nprint(sum)",
      choices: ["4", "10", "6", "Error"],
      answer: 0,
      explain: "The loop sums only odd numbers (1 and 3), resulting in sum=4."
    }
  ];

  let idx = 0;
  let selected = null;

  const codeEl = document.getElementById('code');
  const choicesEl = document.getElementById('choices');
  const resultEl = document.getElementById('result');
  const explainEl = document.getElementById('explainText');
  const qnumEl = document.getElementById('qnum');

  function getLang() {
    return document.querySelector('input[name="lang"]:checked').value;
  }

  function render() {
    const q = questions[idx];
    qnumEl.textContent = "Question " + (idx+1);
    const lang = getLang();
    codeEl.textContent = (lang === 'js') ? q.codeJS : q.codePy;
    choicesEl.innerHTML = '';
    q.choices.forEach((c, i) => {
      const id = 'opt' + i;
      const wrapper = document.createElement('div');
      wrapper.style.marginTop = '6px';
      wrapper.innerHTML = `<label><input type="radio" name="choice" value="${i}" id="${id}"> ${escapeHtml(c)}</label>`;
      choicesEl.appendChild(wrapper);
    });
    resultEl.textContent = '';
    explainEl.textContent = '';
    selected = null;
    document.querySelectorAll('input[name="choice"]').forEach(r => r.addEventListener('change', e=> selected = parseInt(e.target.value)));
  }

  function escapeHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  document.getElementById('submit').addEventListener('click', ()=>{
    if (selected === null) { resultEl.textContent = "Pick an answer first."; resultEl.style.color = "darkorange"; return; }
    const q = questions[idx];
    if (selected === q.answer) {
      resultEl.textContent = "Correct";
      resultEl.style.color = "green";
    } else {
      resultEl.textContent = "Incorrect";
      resultEl.style.color = "red";
    }
  });

  document.getElementById('next').addEventListener('click', ()=>{
    idx = (idx + 1) % questions.length;
    render();
  });

  document.getElementById('explain').addEventListener('click', ()=>{
    explainEl.textContent = questions[idx].explain;
  });

  document.querySelectorAll('input[name="lang"]').forEach(r=> r.addEventListener('change', render));

  render();
})();
</script>
