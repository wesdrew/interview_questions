from Tests import test_poll as test_poll
from Tests import test_is_empty as test_is_empty
from Tests import test_iter as test_iter
from Tests import test_peek as test_peek
from Tests import test_swim as test_swim
from Tests import test_final as test_final
from Tests import test_data as test_data
from Tests import test_str as test_str
from MinPQ import MinPQ as MinPQ

print "Testing MinPQ functions..."
test_poll.test(MinPQ())
test_is_empty.test(MinPQ())
test_peek.test(MinPQ())
test_swim.test(MinPQ())
test_iter.test(MinPQ())
test_final.test(MinPQ(), test_data.objects)
test_str.test(MinPQ())
