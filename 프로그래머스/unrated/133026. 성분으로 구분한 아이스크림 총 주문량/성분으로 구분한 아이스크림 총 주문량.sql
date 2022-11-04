select ice.ingredient_type, sum(first.total_order) as total_order from icecream_info ice
join first_half first
on ice.flavor = first.flavor
group by ice.ingredient_type
order by total_order