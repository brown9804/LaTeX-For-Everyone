function Link(link)
  if not link.target:match("^%a[%w+.-]*:") and not link.target:match("^//") then
    link.target = link.target:gsub("%.md(#.*)$", ".html%1")
    link.target = link.target:gsub("%.md$", ".html")
  end
  return link
end
