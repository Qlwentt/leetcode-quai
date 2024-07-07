<h2><a href="https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/">2730. Find the Longest Semi-Repetitive Substring</a></h2><h3>Medium</h3><hr><div><p>You are given a digit string <code>s</code> that consists of digits from 0 to 9.</p>

<p>A string is called <strong>semi-repetitive</strong> if there is <strong>at most</strong> one adjacent pair of the same digit. For example, <code>"0010"</code>, <code>"002020"</code>, <code>"0123"</code>, <code>"2002"</code>, and <code>"54944"</code> are semi-repetitive while the following are not: <code>"00101022"</code> (adjacent same digit pairs are 00 and 22), and <code>"1101234883"</code> (adjacent same digit pairs are 11 and 88).</p>

<p>Return the length of the <strong>longest semi-repetitive <span data-keyword="substring-nonempty">substring</span></strong> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "52233"</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repetitive substring is "5223". Picking the whole string "52233" has two adjacent same digit pairs 22 and 33, but at most one is allowed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "5494"</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p><code>s</code> is a semi-repetitive string.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "1111111"</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repetitive substring is "11". Picking the substring "111" has two adjacent same digit pairs, but at most one is allowed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>'0' &lt;= s[i] &lt;= '9'</code></li>
</ul>
</div>