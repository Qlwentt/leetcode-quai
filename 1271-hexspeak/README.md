<h2><a href="https://leetcode.com/problems/hexspeak/">1271. Hexspeak</a></h2><h3>Easy</h3><hr><div><p>A decimal number can be converted to its <strong>Hexspeak representation</strong> by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit <code>'0'</code> with the letter <code>'O'</code>, and the digit <code>'1'</code> with the letter <code>'I'</code>. Such a representation is valid if and only if it consists only of the letters in the set <code>{'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}</code>.</p>

<p>Given a string <code>num</code> representing a decimal integer <code>n</code>, <em>return the <strong>Hexspeak representation</strong> of </em><code>n</code><em> if it is valid, otherwise return </em><code>"ERROR"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = "257"
<strong>Output:</strong> "IOI"
<strong>Explanation:</strong> 257 is 101 in hexadecimal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = "3"
<strong>Output:</strong> "ERROR"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 12</code></li>
	<li><code>num</code> does not contain leading zeros.</li>
	<li>num represents an integer in the range <code>[1, 10<sup>12</sup>]</code>.</li>
</ul>
</div>