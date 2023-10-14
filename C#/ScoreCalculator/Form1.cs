using System.Collections;
using System.Windows.Forms.Design;

namespace ScoreCalculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // we need to keep track of scores...
        ArrayList scores = new ArrayList();

        private int getScoresSum()
        {
            int count = 0;
            for (int i = 0; i < scores.Count; i++)
            {
                count += (int)scores[i];
            }
            return count;
        }

        private int getScoresCount()
        {
            return scores.Count;
        }

        private int getScoresAverage()
        {
            int scoresCount = getScoresCount();
            if (scoresCount == 0)
            {
                return 0;
            }
            return getScoresSum() / scoresCount;
        }

        private void clearAllTextBoxes()
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int newScore = Int32.Parse(textBox1.Text.ToString());
            scores.Add(newScore);
            textBox1.Clear();
            textBox2.Text = getScoresSum().ToString();
            textBox3.Text = getScoresCount().ToString();
            textBox4.Text = getScoresAverage().ToString();
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            scores.Clear();
            clearAllTextBoxes();
        }
    }
}