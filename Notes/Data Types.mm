
<map version="0.9.0">
    <node TEXT="Data Types" FOLDED="false">
        <edge COLOR="#b4b4b4" />
        <font NAME="Helvetica" SIZE="10" />
        <node TEXT="Lists" FOLDED="false" POSITION="left">
            <edge COLOR="#988ee3" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="Are mutable (if you change it, old list is gone)" FOLDED="false">
                <edge COLOR="#8f8de3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="lists retain order in which built" FOLDED="false">
                <edge COLOR="#8c92e4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="are 0 indexed" FOLDED="false">
                <edge COLOR="#a28ae0" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Numbers" FOLDED="false" POSITION="right">
            <edge COLOR="#e68782" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="float" FOLDED="false">
                <edge COLOR="#e37978" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="Integer (incl long integer)" FOLDED="false">
                <edge COLOR="#e57f7d" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="decimal" FOLDED="false">
                <edge COLOR="#e48787" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="fraction" FOLDED="false">
                <edge COLOR="#e7977e" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="complex" FOLDED="false">
                <edge COLOR="#e48178" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Number Operations - same as boolean... I think" FOLDED="false" POSITION="right">
            <edge COLOR="#e68782" />
            <font NAME="Helvetica" SIZE="10" />
        </node>
        <node TEXT="List Operations" FOLDED="false" POSITION="left">
            <edge COLOR="#988ee3" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="append - adds item to list" FOLDED="false">
                <edge COLOR="#a190e2" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="pop: deletes (pops off) last element of list" FOLDED="false">
                <edge COLOR="#aa91e2" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="length of list = len(li)" FOLDED="false">
                <edge COLOR="#868ade" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="check if 1 is in list li = 1 in li  (returns True if in list)" FOLDED="false">
                <edge COLOR="#a995e3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="select range between index 1 and 3 = li[1:3] 
returns 2nd and 3rd elements 
(omits 4th element which has index of 3)" FOLDED="false">
                <edge COLOR="#a199e3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="delete the 3rd item = del li[2]" FOLDED="false">
                <edge COLOR="#9884e2" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="select every second entry (step by 2) = li[::2]" FOLDED="false">
                <edge COLOR="#9c95e3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="reverse list li[::-1]" FOLDED="false">
                <edge COLOR="#9e94e6" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Booleans" FOLDED="false" POSITION="right">
            <edge COLOR="#67d7c4" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="True" FOLDED="false">
                <edge COLOR="#65d6cd" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="False" FOLDED="false">
                <edge COLOR="#65d6c8" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Dictionaries" FOLDED="false" POSITION="left">
            <edge COLOR="#9ed56b" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="Order of pairs in dictionary is NOT preserved" FOLDED="false">
                <edge COLOR="#89d36e" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="stores key: value pairs" FOLDED="false">
                <edge COLOR="#a9d364" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="can get list of keys with object.keys" FOLDED="false">
                <edge COLOR="#b5d574" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="can get values with object.values" FOLDED="false">
                <edge COLOR="#9bd362" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="get single element with object.get" FOLDED="false">
                <edge COLOR="#93d065" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Tuples " FOLDED="false" POSITION="left">
            <edge COLOR="#efa670" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="Is immutable (modifications do not canibalize original list)" FOLDED="false">
                <edge COLOR="#efb663" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="cannot append tuples, but can add" FOLDED="false">
                <edge COLOR="#f0bf78" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="retain order" FOLDED="false">
                <edge COLOR="#ef9575" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Boolean Operations" FOLDED="false" POSITION="right">
            <edge COLOR="#67d7c4" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="Comparison" FOLDED="false">
                <edge COLOR="#6bdabd" />
                <font NAME="Helvetica" SIZE="10" />
                <node TEXT="equivalent to ==" FOLDED="false">
                    <edge COLOR="#6dd9d1" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="not equal to !=" FOLDED="false">
                    <edge COLOR="#72dcbb" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="greater than &gt;" FOLDED="false">
                    <edge COLOR="#66d8b8" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="less than &lt;" FOLDED="false">
                    <edge COLOR="#69d9c7" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="greater than or equal to &gt;=" FOLDED="false">
                    <edge COLOR="#6bd7bd" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="less than or equal to &lt;=" FOLDED="false">
                    <edge COLOR="#69d9d1" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
            </node>
            <node TEXT="Logic" FOLDED="false">
                <edge COLOR="#6fdab4" />
                <font NAME="Helvetica" SIZE="10" />
                <node TEXT="not" FOLDED="false">
                    <edge COLOR="#6ad89f" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="and" FOLDED="false">
                    <edge COLOR="#75dbca" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="or" FOLDED="false">
                    <edge COLOR="#75d9bc" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
            </node>
            <node TEXT="Arithmetic" FOLDED="false">
                <edge COLOR="#61d2d4" />
                <font NAME="Helvetica" SIZE="10" />
                <node TEXT="add +" FOLDED="false">
                    <edge COLOR="#69d3cb" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="minus -" FOLDED="false">
                    <edge COLOR="#5dd1d0" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="multiply *" FOLDED="false">
                    <edge COLOR="#61c8d5" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="divide /" FOLDED="false">
                    <edge COLOR="#66c5d4" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="modulo (returns remainder of a division problem) %" FOLDED="false">
                    <edge COLOR="#5cd0c7" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
            </node>
        </node>
        <node TEXT="Sets" FOLDED="false" POSITION="left">
            <edge COLOR="#7aa3e5" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="create with () or {}" FOLDED="false">
                <edge COLOR="#7aa0e4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="Do not retain order" FOLDED="false">
                <edge COLOR="#7094e2" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="allow only unique entries" FOLDED="false">
                <edge COLOR="#77b0e3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="Intersection, union, difference work like mathematical sets" FOLDED="false">
                <edge COLOR="#7e9ee4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="Intersection symbol is &amp;" FOLDED="false">
                <edge COLOR="#7fbae7" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="Union symbol is |" FOLDED="false">
                <edge COLOR="#739ee3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="subtraction symbol  is - (finds elements in the first set that are not in the second set)" FOLDED="false">
                <edge COLOR="#7ab6e4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Strings" FOLDED="false" POSITION="left">
            <edge COLOR="#ebd95f" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="are 0 indexed" FOLDED="false">
                <edge COLOR="#e8cb55" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="String Operations" FOLDED="false" POSITION="left">
            <edge COLOR="#ebd95f" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="concatonate +" FOLDED="false">
                <edge COLOR="#eee067" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="String Methods" FOLDED="false" POSITION="left">
            <edge COLOR="#ebd95f" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="format()  - substitute values" FOLDED="false">
                <edge COLOR="#eccd63" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
    </node>
</map>