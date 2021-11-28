import java.util.ArrayList;
import java.util.List;

/**
 * A text editor is a type of computer program that edits plain text. It
 * consists of a string with a cursor. In the initial state the string is empty
 * with the cursor at the beginning of the string.
 * 
 * Your task is to simulate the working process of a text editor which can
 * handle four types of operations:
 * 
 * TYPE <text> - insert <text> after the current position of the cursor, where
 * <text> consists of at most 20 characters. The cursor moves to the end of the
 * inserted text.
 * 
 * MOVE_CURSOR <offset> - change the current cursor's position. The offset
 * specifies the direction and the value change - if it's negative the cursor
 * moves to the left, and if it's positive the cursor moves to the right. At all
 * times, the cursor is either located at the beginning of the string (before
 * the first character), between two characters, or at the end of the string
 * (after the last character) - the cursor should always be within the text
 * bounds. If the offset is larger than cursor can move, the cursor will move
 * towards the direction as much, as it can. If the cursor does not change its
 * position after the operation, the operation is considered unsuccessful.
 * 
 * SELECT <start_index> <end_index> - select the substring of the current text
 * [text[start_index] ... text[end_index]] (inclusive indices, 0-based) of
 * length end_index - start_index + 1. It is guaranteed that the indices are
 * valid. The cursor changes its position to the end of the selected area. If
 * the next immediately subsequent operation is not TYPE then the selected area
 * is cleared.
 * 
 * If the next immediately subsequent operation is TYPE then the following
 * updating process is expected during the TYPE operation:
 * 
 * Delete the selected text. Insert the new text in the place of the deleted
 * text. The cursor position should move to the end of the typed text. If this
 * operation is anything other than TYPE, the selected area is cleared (See the
 * examples for details).
 * 
 * UNDO - undo the last successful TYPE or MOVE_CURSOR operation (if there is
 * nothing to undo, this operation does nothing). You cannot undo a SELECT
 * operation. UNDO operation returns back to the text and cursor position to the
 * state, they were before the operations is undone. Note that it's not possible
 * to undo the same operation twice: if the operation has been undone, it's
 * undone forever. However, it is possible to undo several operations one by
 * one.
 * 
 * You are given operations, an array of strings where each is an operation of
 * one of the four types above. Your task is to find the resulting text after
 * performing the given operations.
 * 
 * NOTE: An operation is considered successful if the text or the cursor
 * position is changed. For example, moving the cursor to the left when it
 * stands before all characters is not considered a successful operation.
 * 
 * Example
 * 
 * For operations = ["TYPE Code", "TYPE Signal", "MOVE_CURSOR -3", "SELECT 5 8",
 * "TYPE ou", "UNDO", "TYPE nio"], the output should be
 * implementTextEditor(operations) = "CodeSignaniol".
 * 
 * Initially the text is empty, After the "TYPE Code" operation, the text is
 * "Code|" (where the | symbol represents the cursor position), After the "TYPE
 * Signal" operation, the text is "CodeSignal|", After the "MOVE_CURSOR -3", the
 * cursor moves three symbols back, so the text is "CodeSig|nal", After the
 * "SELECT 5 8" operation, the selected text is "igna", the cursor is moved to
 * the end of selected area "CodeSigna|l", After the "TYPE ou" operation, since
 * the previous operation was "SELECT", the selected text is deleted and
 * replaced with the text "ou", the cursor stays after the typed text, so the
 * text is "CodeSou|l", After the "UNDO" operation, the last operation "TYPE" is
 * undone and text and cursor is back as it was before the "TYPE" operation, so
 * the text is "CodeSigna|l", After the "TYPE nio" operation, the text is
 * "CodeSignanio|l", So the final string is "CodeSignaniol". For operations =
 * ["TYPE MyCat", "SELECT 2 3", "MOVE_CURSOR -1", "TYPE he", "SELECT 0 1", "TYPE
 * His"], the output should be implementTextEditor(operations) = "HisCheat".
 * 
 * Initially the text is empty, After the "TYPE MyCat" operation, the text is
 * "MyCat|", After the "SELECT 2 3" operation, the selected text is "Ca", the
 * cursor is moved after the selected area "MyCa|t", After the "MOVE_CURSOR -1",
 * the cursor moves one symbol back, so the text is "MyC|at". Also, the selected
 * area is cleared, as this operation is not "TYPE". No area is selected, After
 * the "TYPE he" operation, the text is "MyChe|at", the typed text is inserted
 * where the cursor stands. After the "SELECT 0 1" operation, the selected text
 * is "My", After the "TYPE His" operation, since the previous operation was
 * "SELECT", the selected text is deleted and replaced with the text "His", the
 * cursor moves to the end of the typed area, so the text is "His|Cheat", So the
 * final string is "HisCheat". For operations = ["TYPE Nothing", "TYPE Is",
 * "TYPE Permanent", "UNDO", "UNDO", "UNDO", "UNDO"], the output should be
 * implementTextEditor(operations) = "".
 * 
 * Initially the text is empty, After the "TYPE Nothing", "TYPE is", and "TYPE
 * Permanent" operations the text is "NothingIsPermanent", Then, after three
 * consequent "UNDO" operations, the text becomes "", the last "UNDO" operation
 * is ignored since there are no more operations to undo. Input/Output
 * 
 * [execution time limit] 3 seconds (java)
 * 
 * [input] array.string operations
 * 
 * A sequence of operations. It's guaranteed that all the operations satisfy the
 * format described above.
 * 
 * Guaranteed constraints: 1 ? operations.length ? 103.
 * 
 * [output] string
 * 
 * The resulting text after performing the given sequence of operations.
 * 
 * TYPE Code TYPE Signal MOVE_CURSOR -3 SELECT 5 8 TYPE ou UNDO
 * 
 */

class TextEditor {

    public static void main(String[] args) {
        String[] operations = { "TYPE Code", "TYPE Signal", "MOVE_CURSOR -3", "SELECT 5 8", "TYPE ou", "UNDO" };

        TextEditor te = new TextEditor();
        System.out.println(te.implementTextEditor(operations));
    }

    class State {
        int cursor;
        String operation;
        String text;
        boolean success;

        State(int cursor, String operation, String text, boolean success) {
            this.cursor = cursor;
            this.operation = operation;
            this.text = text;
            this.success = success;
        }

        int getCursor() {
            return cursor;
        }

        String getOperation() {
            return operation;
        }

        String getText() {
            return text;
        }

    }

    String implementTextEditor(String[] operations) {
        List<State> results = new ArrayList<>();
        String current = "";
        int cursor = 0, selectionStart = -1;
        boolean selected = false;

        for (String operation : operations) {

            System.out.println(operation);
            int space = operation.indexOf(" ");

            String opcode = space >= 0 ? operation.substring(0, space) : operation;
            String param = space >= 0 ? operation.substring(space + 1) : "";

            switch (opcode) {
            case "TYPE": {
                current = current.substring(0, cursor - (selected ? cursor - selectionStart : 0)) + param
                        + current.substring(cursor);
                cursor += param.length();
                results.add(new State(cursor, opcode, current, true));
                selected = false;
            }
                break;
            case "MOVE_CURSOR": {
                int offset = Integer.parseInt(param.trim());

                int newPosition = cursor + offset;

                if (newPosition < 0) {
                    newPosition = 0;
                } else if (newPosition > current.length() - 1) {
                    newPosition = current.length() - 1;
                }

                if (newPosition != cursor) {
                    cursor = newPosition;
                    results.add(new State(cursor, opcode, current, true));
                }

            }
                break;
            case "SELECT": {
                String[] indexes = param.trim().split(" ");
                selectionStart = Integer.parseInt(indexes[0]);
                cursor = Integer.parseInt(indexes[1]);
                results.add(new State(cursor, opcode, current, true));
            }
                break;
            case "UNDO": {
                boolean done = false;
                int i = results.size() - 1;
                while (i >= 0 && !done) {
                    State previous = results.get(i);
                    if ("TYPE".equals(previous.getOperation()) || "MOVE_CURSOR".equals(previous.getOperation())) {
                        if (i > 0) {
                            State newState = results.get(i - 1);
                            cursor = newState.getCursor();
                            current = newState.getText();
                            results = results.subList(0, i - 1);
                        } else {
                            results = new ArrayList();
                            current = "";
                            cursor = 0;
                        }
                        done = true;
                    }
                    i--;
                }
            }
                break;
            }
        }

        return current;
    }
}