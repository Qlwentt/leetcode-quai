<h2><a href="https://leetcode.com/problems/before-and-after-puzzle/">1181. Before and After Puzzle</a></h2><h3>Medium</h3><hr><div><p>Given a list of <code>phrases</code>, generate a list of&nbsp;Before and After puzzles.</p>

<p>A <em>phrase</em> is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are&nbsp;no consecutive spaces&nbsp;in a phrase.</p>

<p><em>Before and After&nbsp;puzzles</em> are phrases that are formed by merging&nbsp;two phrases where the <strong>last&nbsp;word of the first&nbsp;phrase</strong> is the same as the <strong>first word of the second phrase</strong>.</p>

<p>Return the&nbsp;Before and After&nbsp;puzzles that can be formed by every two phrases&nbsp;<code>phrases[i]</code>&nbsp;and&nbsp;<code>phrases[j]</code>&nbsp;where&nbsp;<code>i != j</code>. Note that the order of matching two phrases matters, we want to consider both orders.</p>

<p>You should return a list of&nbsp;<strong>distinct</strong>&nbsp;strings <strong>sorted&nbsp;lexicographically</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> phrases = ["writing code","code rocks"]
<strong>Output:</strong> ["writing code rocks"]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> phrases = ["mission statement",
                  "a quick bite to eat",
&nbsp;                 "a chip off the old block",
&nbsp;                 "chocolate bar",
&nbsp;                 "mission impossible",
&nbsp;                 "a man on a mission",
&nbsp;                 "block party",
&nbsp;                 "eat my words",
&nbsp;                 "bar of soap"]
<strong>Output:</strong> ["a chip off the old block party",
&nbsp;        "a man on a mission impossible",
&nbsp;        "a man on a mission statement",
&nbsp;        "a quick bite to eat my words",
         "chocolate bar of soap"]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> phrases = ["a","b","a"]
<strong>Output:</strong> ["a"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= phrases.length &lt;= 100</code></li>
	<li><code>1 &lt;= phrases[i].length &lt;= 100</code></li>
</ul>
</div>