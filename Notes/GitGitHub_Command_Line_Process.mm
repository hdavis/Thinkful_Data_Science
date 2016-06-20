
<map version="0.9.0">
    <node TEXT="Git/GitHub 
Command Line Process" FOLDED="false">
        <edge COLOR="#b4b4b4" />
        <font NAME="Helvetica" SIZE="10" />
        <node TEXT="Set up new repo on local computer
(use Terminal or Windows command line)" FOLDED="false" POSITION="right">
            <edge COLOR="#7aa3e5" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="Navigate to directory of files to commit" FOLDED="false">
                <edge COLOR="#77abe5" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="git init" FOLDED="false">
                <edge COLOR="#7da9e3" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="git add . (adds all files in directory)" FOLDED="false">
                <edge COLOR="#7eb0e6" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="git commit -m &quot;Initial commit&quot;" FOLDED="false">
                <edge COLOR="#7c9ae4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="Save local snapshot to GitHub" FOLDED="false" POSITION="right">
            <edge COLOR="#988ee3" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="In web-based GitHub acct, create new repository (+ in upper right of screen), label same name as local Git repo." FOLDED="false">
                <edge COLOR="#9490e4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="Follow instructions for &quot;push existing repo from command line&quot;" FOLDED="false">
                <edge COLOR="#9295e2" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="1) git remote add origin https://github.com/ ..." FOLDED="false">
                <edge COLOR="#9193e5" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
            <node TEXT="2) git push -u origin master (may need to enter username and password)" FOLDED="false">
                <edge COLOR="#998be4" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
        <node TEXT="git status 
(to check status of repo)" FOLDED="false" POSITION="left">
            <edge COLOR="#ebd95f" />
            <font NAME="Helvetica" SIZE="10" />
        </node>
        <node TEXT="Make commits to an EXISTING repo" FOLDED="false" POSITION="right">
            <edge COLOR="#efa670" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="add file(s)" FOLDED="false">
                <edge COLOR="#eebd76" />
                <font NAME="Helvetica" SIZE="10" />
                <node TEXT="git add filename.py" FOLDED="false">
                    <edge COLOR="#eea471" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
            </node>
            <node TEXT="commit file(s)" FOLDED="false">
                <edge COLOR="#ee9778" />
                <font NAME="Helvetica" SIZE="10" />
                <node TEXT="git commit -m &quot;Create filename.py&quot;" FOLDED="false">
                    <edge COLOR="#ec8a73" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
                <node TEXT="git commit -am '&lt;commit_message&gt;' (-a adds all changes to previously committed files - saves having to add them explicitly with git add ...)" FOLDED="false">
                    <edge COLOR="#ed776e" />
                    <font NAME="Helvetica" SIZE="10" />
                </node>
            </node>
        </node>
        <node TEXT="Pull code from GitHub" FOLDED="false" POSITION="left">
            <edge COLOR="#9ed56b" />
            <font NAME="Helvetica" SIZE="10" />
            <node TEXT="git pull origin master" FOLDED="false">
                <edge COLOR="#a8d564" />
                <font NAME="Helvetica" SIZE="10" />
            </node>
        </node>
    </node>
</map>