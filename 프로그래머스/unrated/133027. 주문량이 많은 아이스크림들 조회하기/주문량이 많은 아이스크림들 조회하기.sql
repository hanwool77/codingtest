select first.flavor from first_half first
join july july on first.flavor = july.flavor
group by first.flavor
order by sum(first.total_order) + sum(july.total_order) desc
limit 3;