using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppChat
{
    public class User
    {
        private string userName;
        private string passWord;

        public string UserName { get => userName; set => userName = value; }
        public string PassWord { get => passWord; set => passWord = value; }

        public User(string userName, string passWord)
        {
            this.UserName = userName;
            this.PassWord = passWord;
        }
    }
}
