import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class jse_191209_0610 {

    public static void main(String[] args) {
        SimpleGUI app = new SimpleGUI();
        app.setVisible(true);
    }
}

/**
 * Example of Simple Swing GUI application
 */
class SimpleGUI extends JFrame {
    private JButton button = new JButton("Press");
    private JTextField input = new JTextField("", 5);
    private JLabel label = new JLabel("Input:");
    private JRadioButton radio1 = new JRadioButton("Select this");
    private JRadioButton radio2 = new JRadioButton("Select this");
    private JCheckBox check = new JCheckBox("Input:", false);

    public SimpleGUI() {
        super("Simple Example");
        this.setBounds(100, 100, 250, 100);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(3, 2, 2, 2));
        container.add(label);
        container.add(input);

        ButtonGroup group = new ButtonGroup();
        group.add(radio1);
        group.add(radio2);
        container.add(radio1);
        container.add(radio2);
        radio1.setSelected(true);
        container.add(check);
        button.addActionListener(new ButtonEventListener());
        container.add(button);
    }

    class ButtonEventListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String message = "";
            message += "Button has been pressed\n";
            message += "Text is " + input.getText() + "\n";
            message += (radio1.isSelected() ? "Radio #1" : "Radio #2");
            message += " is selected\n";
            message += "Checkbox is " + ((check.isSelected()) ? "checled" : "unchecked");
            JOptionPane.showMessageDialog(
                    null,
                    message,
                    "Output",
                    JOptionPane.PLAIN_MESSAGE
            );
        }
    }
}
