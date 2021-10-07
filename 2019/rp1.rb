$stdout.sync = true

def solve(a, b)
  m = (a + b) / 2
  puts m
  $stdout.flush
  s = STDIN.gets.chomp
  if s.eql? "CORRECT"
    return
  elsif s.eql? "TOO_SMALL"
    solve(m + 1, b)
  else
    solve(a, m - 1)
  end
end

t = STDIN.gets.chomp.to_i
ks = 1
while ks <= t
  a, b = STDIN.gets.split.map &:to_i;
  n = STDIN.gets.chomp.to_i
  solve(a + 1, b)
  ks = ks + 1
end
