<h2><a href="https://leetcode.com/problems/add-bold-tag-in-string/">616. Add Bold Tag in String</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>s</code> and an array of strings <code>words</code>.</p>

<p>You should add a closed pair of bold tag <code>&lt;b&gt;</code> and <code>&lt;/b&gt;</code> to wrap the substrings in <code>s</code> that exist in <code>words</code>.</p>

<ul>
	<li>If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.</li>
	<li>If two substrings wrapped by bold tags are consecutive, you should combine them.</li>
</ul>

<p>Return <code>s</code> <em>after adding the bold tags</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abcxyz123", words = ["abc","123"]
<strong>Output:</strong> "&lt;b&gt;abc&lt;/b&gt;xyz&lt;b&gt;123&lt;/b&gt;"
<strong>Explanation:</strong> The two strings of words are substrings of s as following: "<u>abc</u>xyz<u>123</u>".
We add &lt;b&gt; before each substring and &lt;/b&gt; after each substring.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aaabbb", words = ["aa","b"]
<strong>Output:</strong> "&lt;b&gt;aaabbb&lt;/b&gt;"
<strong>Explanation:</strong> 
"aa" appears as a substring two times: "<u>aa</u>abbb" and "a<u>aa</u>bbb".
"b" appears as a substring three times: "aaa<u>b</u>bb", "aaab<u>b</u>b", and "aaabb<u>b</u>".
We add &lt;b&gt; before each substring and &lt;/b&gt; after each substring: "&lt;b&gt;a&lt;b&gt;a&lt;/b&gt;a&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;".
Since the first two &lt;b&gt;'s overlap, we merge them: "&lt;b&gt;aaa&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;&lt;b&gt;b&lt;/b&gt;".
Since now the four &lt;b&gt;'s are consecutive, we merge them: "&lt;b&gt;aaabbb&lt;/b&gt;".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>0 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 1000</code></li>
	<li><code>s</code> and <code>words[i]</code> consist of English letters and digits.</li>
	<li>All the values of <code>words</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 758: <a href="https://leetcode.com/problems/bold-words-in-string/" target="_blank">https://leetcode.com/problems/bold-words-in-string/</a></p>
</div>