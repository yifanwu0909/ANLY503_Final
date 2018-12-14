m_ideal <- read.csv("m_ideal_m_age.csv")
f_ideal <- read.csv("f_ideal_m_age.csv")

ggplot() + 
  geom_density(data = m_ideal, aes(x = Ideal_Marriage_Age, fill = "Male"), alpha = 0.3) +
  geom_density(data = f_ideal, aes(x = Ideal_Marriage_Age, fill = "Female"), alpha = 0.3) +
  ggtitle("Surveyed Ideal Marriage Age for Both Gender") +
  xlab("Ideal Marriage Age") + 
  scale_fill_discrete(name = "Gender")
