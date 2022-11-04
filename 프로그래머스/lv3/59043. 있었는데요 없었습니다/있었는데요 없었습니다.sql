select ins.animal_id, ins.name from animal_ins ins
join animal_outs outs 
on ins.animal_id = outs.animal_id
where outs.datetime < ins.datetime
order by ins.datetime