# COMPUTATIONAL-GEOMETRY-CODES-CU-2nd-sem-assignment-
1.Slope range counting [O(nlogn)]
2.Covex hull: Graham scan algorithm [O(nlogn)]
3.Covex hull: Jarvis' march / Gift wrapping algorithm [O(nh)]
4.Plane sweep / Line sweep algorithm
5.Polygon triangulation



Plane sweep / Line sweep algorithm:
(1) Insert all of the endpoints of the line segments of S into the event queue. The initial sweep-line status
is empty.
(2) While the event queue is nonempty, extract the next event in the queue. There are three cases,
depending on the type of event:
Left endpoint: 
(a) Insert this line segment s into the sweep-line status, based on the y-coordinate of its left
endpoint.
(b) Let s' and s" be the segments immediately above and below s on the sweep line. If there is
an event associated with this pair, remove it from the event queue.
(c) Test for intersections between s and s' and between s and s" to the right of the sweep line. If
so, add the corresponding event(s) to the event queue.
Right endpoint: 
(a) Let s' and s" be the segments immediately above and below s on the sweep line.
(b) Delete segment s from the sweep-line status.
(c) Test for intersections between s' and s" to the right of the sweep line. If so, add the corresponding event to the event queue.
Intersection: 
(a) Report this intersection.
(b) Let s' and s" be the two intersecting segments. Swap these two line segments in the sweep-line
status (they must be adjacent to each other).
(c) As a result, s' and s" have changed which segments are immediately above and below them.
Remove any old events due to adjacencies that have ended and insert any new intersection events from adjacencies that have been created.
